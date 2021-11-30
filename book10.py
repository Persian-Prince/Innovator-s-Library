>>> # Sample data
>>> data = [
...     ("Linda", "Technical Lead", "linda@example.com"),
...     ("Joe", "Senior Web Developer", "joe@example.com"),
...     ("Lara", "Project Manager", "lara@example.com"),
...     ("David", "Data Analyst", "david@example.com"),
...     ("Jane", "Senior Python Developer", "jane@example.com"),
... ]

>>> # Insert sample data
>>> for name, job, email in data:
...     insertDataQuery.addBindValue(name)
...     insertDataQuery.addBindValue(job)
...     insertDataQuery.addBindValue(email)
...     insertDataQuery.exec()
...
True
True
True
True
True