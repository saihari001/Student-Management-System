# Generated by Django 4.2.5 on 2023-11-15 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_staff_leave'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_leave',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
