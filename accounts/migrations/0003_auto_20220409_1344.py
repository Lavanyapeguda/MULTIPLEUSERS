# Generated by Django 2.2.27 on 2022-04-09 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220409_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='confirmpassword',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='password',
        ),
    ]
