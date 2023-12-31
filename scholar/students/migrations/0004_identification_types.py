# Generated by Django 4.2.5 on 2023-11-08 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_remove_user_dni_user_created_at_user_deleted_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='identification_types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('abrev', models.CharField(max_length=10)),
                ('descrip', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('update_at', models.DateTimeField(default=datetime.datetime.now)),
                ('deleted_at', models.DateTimeField(null=True)),
            ],
        ),
    ]
