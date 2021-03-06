# Generated by Django 2.1.4 on 2020-03-27 16:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_time', models.TimeField(default=django.utils.timezone.now, verbose_name=' Время брони c ')),
                ('booked_time', models.TimeField(blank=True, null=True, verbose_name='Время брони до')),
                ('status', models.CharField(blank=True, max_length=64, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='RoomProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(blank=True, max_length=64, verbose_name='Название ')),
                ('seets_count', models.PositiveIntegerField(default=0, verbose_name='Количество мест')),
                ('projector', models.BooleanField(default=True, verbose_name='Наличие проектора')),
                ('desk', models.BooleanField(default=True, verbose_name='Наличие доски')),
                ('status', models.CharField(blank=True, max_length=64, verbose_name='Статус')),
            ],
        ),
        migrations.AddField(
            model_name='bookingprofile',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.RoomProfile'),
        ),
    ]
