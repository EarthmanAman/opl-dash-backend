# Generated by Django 4.0.4 on 2022-07-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_rename_amount_req_sale_amount_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
