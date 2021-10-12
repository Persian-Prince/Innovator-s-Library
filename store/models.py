from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(null=True, blank=True)
    # Available true means that the copy is available for issue, False means unavailable
    available = models.BooleanField(default=True)
    borrower = models.ForeignKey(User, related_name='borrower', null=True, blank=True, on_delete=models.SET_NULL)

    def str(self):
        if self.available:
            return f'{self.book.title} - Available'
        else:
            return f'{self.book.title}, {str(self.borrow_date)}'

