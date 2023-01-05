from django.utils import timezone
from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
class Books(models.Model):
    author = models.CharField(max_length=100)
    title = models.TextField(max_length=100)
    desc = models.TextField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    in_stock = models.BooleanField(default=False)

    def issue(self):
        self.in_stock = True
        self.save()
    
    def get_absolute_url(self):
        return reverse('basicApp:books_list')

    def __str__(self):
        return self.title


class IssuedBooks(models.Model):
    noOfDays = models.DateField(default=datetime.date.today)
    book = models.ForeignKey('basicApp.Books', related_name='issuedBooks', on_delete=models.CASCADE, db_constraint=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, db_constraint=False)
    user_id = models.AutoField

    def get_absolute_url(self):
        return reverse('basicApp:books_list')

    def __str__(self):
        return str(self.book)