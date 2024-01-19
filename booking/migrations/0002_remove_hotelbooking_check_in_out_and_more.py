# Generated by Django 5.0 on 2024-01-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotelbooking',
            name='check_in_out',
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='check_in',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='hotelbooking',
            name='check_out',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.DeleteModel(
            name='CheckInOut',
        ),
    ]
