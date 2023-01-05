# Generated by Django 4.0.2 on 2022-05-11 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicApp', '0006_alter_issuedbooks_book_alter_issuedbooks_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('commit_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('commitedRepo', models.CharField(max_length=100)),
                ('commitTitle', models.CharField(max_length=50)),
                ('textFile', models.URLField(blank=True)),
                ('videoFile', models.URLField(blank=True)),
                ('imageFile', models.ImageField(blank=True, upload_to='')),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('commmitedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commitedUser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Repositories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(choices=[('Chemistry', 'Chemistry'), ('Robotics', 'Robotics'), ('Phychology', 'Phychology')], max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('createdDate', models.DateTimeField(default=django.utils.timezone.now)),
                ('progress_title', models.CharField(max_length=100)),
                ('progress_detail', models.TextField(blank=True, null=True)),
                ('progress_video', models.URLField(blank=True, null=True)),
                ('progress_image', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='repoOwner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='issuedbooks',
            name='book',
        ),
        migrations.RemoveField(
            model_name='issuedbooks',
            name='user',
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='IssuedBooks',
        ),
    ]
