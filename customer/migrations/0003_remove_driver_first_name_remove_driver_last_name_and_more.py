# Generated by Django 4.0.4 on 2022-07-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_truck_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='last_name',
        ),
        migrations.AddField(
            model_name='driver',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]