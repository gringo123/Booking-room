# Generated by Django 2.1.4 on 2020-04-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_bookingprofile_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomprofile',
            name='status',
        ),
        migrations.AddField(
            model_name='roomprofile',
            name='condition',
            field=models.BooleanField(default=True, verbose_name='Наличие Кондиционера'),
        ),
    ]
