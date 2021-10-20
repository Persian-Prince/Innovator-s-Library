from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    description = models.TextField(null=True)
    mrp = models.PositiveIntegerField()
    rating = models.FloatField(default=0.0)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return f'{self.title} by {self.author}'


class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(null=True, blank=True)
    # Available true means that the copy is available for issue, False means unavailable
    available = models.BooleanField(default=True)
    borrower = models.ForeignKey(User, related_name='borrower', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        if self.available:
            return f'{self.book.title} - Available'
        else:
            return f'{self.book.title}, {str(self.borrow_date)}'

class Review(models.Model):
    book_reviewed = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField(
        default=1,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
     ) 
    reviewer = models.ForeignKey(User, related_name='reviewer', null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.rating}: {self.book_reviewed} by User {self.reviewer}' 
