# Generated by Django 3.1.4 on 2021-01-13 10:25

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, null=True, region=None),
        ),
    ]
