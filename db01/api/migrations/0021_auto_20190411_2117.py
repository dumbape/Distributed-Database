# Generated by Django 2.1.7 on 2019-04-11 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20190409_0650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotelbooking',
            old_name='check_in',
            new_name='in_date',
        ),
        migrations.RenameField(
            model_name='hotelbooking',
            old_name='check_out',
            new_name='out_date',
        ),
        migrations.RemoveField(
            model_name='hotelbooking',
            name='area',
        ),
        migrations.RemoveField(
            model_name='hotelbooking',
            name='city',
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
