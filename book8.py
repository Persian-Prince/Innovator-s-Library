>>> from rpcontacts.database import createConnection

>>> # Create a connection
>>> createConnection("contacts.sqlite")
True

>>> # Confirm that contacts table exists
>>> from PyQt5.QtSql import QSqlDatabase
>>> db = QSqlDatabase.database()
>>> db.tables()
['contacts', 'sqlite_sequence']