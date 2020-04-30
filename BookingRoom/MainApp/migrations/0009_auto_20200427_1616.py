# Generated by Django 2.1.4 on 2020-04-27 12:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_bookingprofile_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingprofile',
            name='booked_time',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время брони до'),
        ),
        migrations.AlterField(
            model_name='bookingprofile',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.RoomProfile', verbose_name='Book'),
        ),
    ]