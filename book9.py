>>> # Prepare a query to insert sample data
>>> from PyQt5.QtSql import QSqlQuery

>>> insertDataQuery = QSqlQuery()
>>> insertDataQuery.prepare(
...     """
...     INSERT INTO contacts (
...         name,
...         job,
...         email
...     )
...     VALUES (?, ?, ?)
...     """
... )
True