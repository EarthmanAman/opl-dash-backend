# Generated by Django 4.0.4 on 2022-05-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sale_truck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='date',
            field=models.DateField(),
        ),
    ]
