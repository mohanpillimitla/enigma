# Generated by Django 2.2.4 on 2020-06-20 04:06

from django.db import migrations
import timezone_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200620_0350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='tz',
            field=timezone_utils.fields.TimeZoneField(default='US/Pacific', max_length=32),
        ),
    ]
