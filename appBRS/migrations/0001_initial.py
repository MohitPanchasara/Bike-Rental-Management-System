# Generated by Django 3.1.4 on 2021-04-16 08:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('bike_number', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('bike_color', models.CharField(choices=[('Red', 'Red'), ('White', 'White'), ('Black', 'Black'), ('Blue', 'Blue')], max_length=20)),
                ('bike_type', models.CharField(choices=[('Regular', 'Regular'), ('Non Gear', 'Non Gear'), ('Sports', 'Sports')], max_length=20)),
                ('bike_model', models.CharField(max_length=30)),
                ('bike_brand', models.CharField(max_length=30)),
                ('bike_available', models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available')], max_length=20)),
                ('bike_user', models.CharField(blank=True, default='NONE', max_length=30)),
                ('bike_rent_number', models.PositiveIntegerField(blank=True, default=1)),
                ('bike_rent', models.CharField(blank=True, choices=[('Hour', 'Hour'), ('Day', 'Day'), ('Week', 'Week')], max_length=30)),
                ('date_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('station_address', models.CharField(max_length=50)),
                ('station_phoneNo', models.CharField(max_length=10)),
                ('bike_quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.CharField(max_length=12)),
                ('proof_of_user', models.CharField(max_length=20)),
                ('user_bike', models.CharField(blank=True, default='NOT TAKEN', max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly_rent', models.PositiveIntegerField()),
                ('daily_rent', models.PositiveIntegerField()),
                ('weekly_rent', models.PositiveIntegerField()),
                ('hourly_penalty', models.PositiveIntegerField()),
                ('daily_penalty', models.PositiveIntegerField()),
                ('weekly_penalty', models.PositiveIntegerField()),
                ('bike_rent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='appBRS.bike')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('Transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_amount', models.PositiveIntegerField()),
                ('Payment_Des', models.CharField(max_length=100)),
                ('Payment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('employee_name', models.CharField(max_length=20)),
                ('employee_phonNo', models.CharField(max_length=10)),
                ('station_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBRS.station')),
            ],
        ),
        migrations.AddField(
            model_name='bike',
            name='bike_station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBRS.station'),
        ),
    ]
