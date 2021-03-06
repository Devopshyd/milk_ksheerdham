# Generated by Django 3.0.7 on 2021-01-22 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200428_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deliveryboy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=12)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('vehicle_numberplate', models.CharField(max_length=10)),
                ('Driving_liecense', models.CharField(max_length=10)),
                ('vehicale_rc', models.CharField(max_length=30)),
                ('Adarcard_number', models.CharField(max_length=30)),
                ('Bank_account_No', models.CharField(max_length=40)),
                ('ifsc_code', models.CharField(max_length=15)),
                ('del_image', models.FileField(upload_to='')),
                ('vehicle_rc_image', models.FileField(upload_to='')),
                ('Adarcard_imge', models.FileField(upload_to='')),
                ('Divingliecense_image', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Deliveryboy_orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Delivery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Deliveryboy')),
            ],
        ),
    ]
