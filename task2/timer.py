import sys
import json
import redis
import time


r = redis.Redis(host='localhost', port=6379, db=0)


def load_data():
    start_time = time.time()

    with open('generated_data.json') as f:
        data = json.load(f)

    for idx, item in enumerate(data, start=1):
        r.set(f'json_data_{idx}', json.dumps(item))

        # Хэши (Hashes)
        user_data = item.get('user', {})
        for key, value in user_data.items():
            r.hset(f'user:{idx}', key, str(value))

        # Списки (Lists)
        tags = user_data.get('tags', [])
        for tag in tags:
            r.lpush(f'user:{idx}:tags', tag)

        # Упорядоченные множества (Sorted Sets)
        products = item.get('products', [])
        for product in products:
            r.zadd(f'products:{idx}', {json.dumps(product): product['price']})

        # Множества (Sets)
        order_ids = item.get('orders', {}).keys()
        r.sadd(f'order_ids:{idx}', *order_ids)

    end_time = time.time()
    print(f"Данные успешно загружены в Redis за {end_time - start_time} секунд.")


def run_queries(num_queries):

    start_time = time.time()

    for idx in range(1, num_queries + 1):
        # Пример запроса к строкам (Strings)
        r.get(f'json_data_{idx}')

        # Пример запроса к хэшу (Hashes)
        r.hgetall(f'user:{idx}')

        # Пример запроса к списку (Lists)
        r.lrange(f'user:{idx}:tags', 0, -1)

        # Пример запроса к упорядоченному множеству (Sorted Sets)
        r.zrange(f'products:{idx}', 0, -1)

        # Пример запроса к множеству (Sets)
        r.smembers(f'order_ids:{idx}')

    end_time = time.time()
    print(f"Выполнение {num_queries} запросов заняло {end_time - start_time} секунд.")


def run_deletion(num_elements):
    start_time = time.time()

    # Удаление данных из Redis
    for idx in range(1, num_elements + 1):
        # Удаление ключей строк (Strings)
        r.delete(f'json_data_{idx}')

        # Удаление хэшей (Hashes)
        r.delete(f'user:{idx}')

        # Удаление списков (Lists)
        r.delete(f'user:{idx}:tags')

        # Удаление упорядоченных множеств (Sorted Sets)
        r.delete(f'products:{idx}')

        # Удаление множеств (Sets)
        r.delete(f'order_ids:{idx}')

    end_time = time.time()
    print(f"Удаление {num_elements} элементов заняло {end_time - start_time} секунд.")


if __name__ == "__main__":
    load_data()

    time.sleep(5)

    if len(sys.argv) < 2:
        print("Не указано количество запросов. Укажите количество запросов через аргумент командной строки.")
        sys.exit(1)

    num_queries = int(sys.argv[1])
    run_queries(num_queries)

    num_elements_to_delete = int(sys.argv[1])
    run_deletion(num_elements_to_delete)
