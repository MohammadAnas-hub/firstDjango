# Generated by Django 4.0.2 on 2022-03-04 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicApp', '0003_issuedbooks_noofdays'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuedbooks',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
