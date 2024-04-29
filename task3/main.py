import xappy

# открытие соединения для индексации с базой поискового индекса
# указывается полный или относительный путь к папке
connection = xappy.IndexerConnection('/path/to/base')

# свойства полей индекса
connection.add_field_action(
    'title', xappy.FieldActions.INDEX_FREETEXT, weight=5, language='ru')
connection.add_field_action(
    'description', xappy.FieldActions.INDEX_FREETEXT, language='ru')