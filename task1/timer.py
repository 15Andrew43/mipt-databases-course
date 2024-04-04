import pymongo
import time

def connect_to_mongodb(host, port, db_name):
    client = pymongo.MongoClient(host, port)
    db = client[db_name]
    return db

def execute_query(collection, query):
    start_time = time.time()
    result = list(collection.find(query))
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def create_index(collection, field):
    collection.create_index([(field, pymongo.ASCENDING)])

def drop_index(collection, field):
    collection.drop_index(field)

if __name__ == "__main__":
    # Параметры подключения к MongoDB
    HOST = 'localhost'
    PORT = 27017
    DB_NAME = 'dbForHW'
    COLLECTION_NAME = 'collectionFotrHW'

    # Подключение к MongoDB
    db = connect_to_mongodb(HOST, PORT, DB_NAME)
    collection = db[COLLECTION_NAME]

    # Примеры запросов
    queries = [
        {"age": {"$gte": 30}},
        {"address.city": "City 1"},
        {"interests": "Books"}
    ]

    # Выполнение запросов и замер времени выполнения без индексов
    print("Executing queries without indexes...")
    for query in queries:
        result, execution_time = execute_query(collection, query)
        print(f"Query: {query}, Execution time: {execution_time:.4f} seconds")

    # Создание индексов и замер времени выполнения с индексами
    print("\nCreating indexes...")
    for query in queries:
        field = list(query.keys())[0]  # Получаем имя поля для индекса
        start_time = time.time()
        create_index(collection, field)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Index created for field: {field} in {execution_time} seconds")

    print("\nExecuting queries with indexes...")
    for query in queries:
        result, execution_time = execute_query(collection, query)
        print(f"Query: {query}, Execution time: {execution_time:.4f} seconds")

    # Удаление индексов и замер времени выполнения после удаления индексов
    print("\nDropping indexes...")
    for query in queries:
        field = list(query.keys())[0]+'_1'  # Получаем имя поля для индекса
        drop_index(collection, field)
        print(f"Index dropped for field: {field}")
