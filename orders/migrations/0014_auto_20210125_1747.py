# Generated by Django 3.0.6 on 2021-01-25 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Order_Date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
