# Generated by Django 2.2.4 on 2020-06-20 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200619_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='end_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='activities',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
