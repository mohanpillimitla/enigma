# Generated by Django 2.2.4 on 2020-06-21 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200620_0411'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity', to='api.Employees'),
        ),
    ]