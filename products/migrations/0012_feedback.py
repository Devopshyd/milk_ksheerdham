# Generated by Django 3.0.6 on 2021-01-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_driver_employee_farm_data_flashoffers_vehicle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('feedback', models.CharField(max_length=500)),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
    ]
