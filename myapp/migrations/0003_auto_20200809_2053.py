# Generated by Django 3.0.5 on 2020-08-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_registeruser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
