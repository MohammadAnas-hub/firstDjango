# Generated by Django 4.0.2 on 2022-05-11 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicApp', '0007_commit_repositories_remove_issuedbooks_book_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='commitedRepo',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='commitedRepo', to='basicApp.repositories'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commit',
            name='commmitedUser',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='commitedUser', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='commit',
            name='createdDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
