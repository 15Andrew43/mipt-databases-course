import redis
import os
import time

# Получаем переменные окружения для подключения к Redis
REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

# Создаем подключение к Redis
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)

# Увеличиваем значение счетчика
counter_key = 'counter'

while True:
    r.incr(counter_key)

    # Получаем текущее значение счетчика и выводим его
    counter_value = r.get(counter_key).decode('utf-8')
    print(f"Текущее значение счетчика: {counter_value}")

    time.sleep(1)
