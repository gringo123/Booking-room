# Generated by Django 2.1.4 on 2020-04-28 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0009_auto_20200427_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingprofile',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MainApp.RoomProfile'),
        ),
    ]