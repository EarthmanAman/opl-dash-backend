# Generated by Django 4.0.4 on 2022-07-16 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_sale_amount_req_sale_loading_date_sale_remarks_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='amount_req',
            new_name='amount_paid',
        ),
    ]