# Generated by Django 3.0.5 on 2020-08-09 13:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='email',
            field=models.EmailField(default=datetime.datetime(2020, 8, 9, 13, 50, 42, 692677, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
    ]
