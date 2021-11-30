>>> query = QSqlQuery()
>>> query.exec("SELECT name, job, email FROM contacts")
True

>>> while query.next():
...     print(query.value(0), query.value(1), query.value(2))
...