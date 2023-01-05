from django.contrib import admin
from .models import Books, IssuedBooks

# Register your models here.
admin.site.register(Books)
admin.site.register(IssuedBooks)