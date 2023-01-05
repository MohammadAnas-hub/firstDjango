from django.contrib import admin
from .models import Repositories, Commit

# Register your models here.
admin.site.register(Repositories)
admin.site.register(Commit)