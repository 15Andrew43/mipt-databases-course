# MongoDB

## Цель:
В результате выполнения ДЗ вы научитесь разворачивать MongoDB, заполнять данными и делать запросы.

## Описание/инструкция выполнения домашнего задания:

1. **Установка MongoDB:**
   - Вы можете выбрать один из следующих способов установки:
     - Локально
     - С использованием Docker
     - Виртуальная машина (облачный сервис)

2. **Заполнение данными:**
   - Используйте один из предложенных датасетов или любой другой подходящий для ваших целей. Примеры датасетов доступны по ссылке: [Примеры датасетов](https://habr.com/ru/company/edison/blog/480408/)

3. **Написание запросов:**
   - Напишите несколько запросов на выборку и обновление данных в вашей базе MongoDB.

4. **Создание индексов и сравнение производительности:**
   - Создайте необходимые индексы для улучшения производительности выполнения запросов.
   - Сравните производительность запросов с индексами и без них.

## Тестирование производительности MongoDB

### Генерация данных
 - Для создания тестовых данных используйте скрипт generator.py.
 - Структуры данных сохраняются в файле data.json.
 
### Импорт данных в MongoDB
 - Данные из файла data.json можно импортировать в MongoDB с помощью команды `mongoimport --host localhost:27017 --db dbForHW --collection collectionForHW --type json --file data.json --jsonArray`

### Тестирование производительности
Для выполнения запросов без индексов а потом с индексами используйте скрипт timer.py.


### Результат

```
Executing queries without indexes...
Query: {'age': {'$gte': 30}}, Execution time: 20.4199 seconds
Query: {'address.city': 'City 1'}, Execution time: 13.5096 seconds
Query: {'interests': 'Books'}, Execution time: 9.2294 seconds

Creating indexes...
Index created for field: age in 6.161764144897461 seconds
Index created for field: address.city in 7.320004940032959 seconds
Index created for field: interests in 12.565794944763184 seconds

Executing queries with indexes...
Query: {'age': {'$gte': 30}}, Execution time: 81.8063 seconds
Query: {'address.city': 'City 1'}, Execution time: 5.1187 seconds
Query: {'interests': 'Books'}, Execution time: 16.5092 seconds

Dropping indexes...
Index dropped for field: age_1
Index dropped for field: address.city_1
Index dropped for field: interests_1
```

### Вывод
Индексы нужно использовать с умом