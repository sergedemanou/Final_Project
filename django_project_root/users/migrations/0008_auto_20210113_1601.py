# Generated by Django 3.1.4 on 2021-01-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210113_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('developpeur_web', 'developpeur_web'), ('developpeur_mobile', 'developpeur_mobile'), ('designer', 'designer'), ('invité', 'invité')], max_length=300),
        ),
    ]