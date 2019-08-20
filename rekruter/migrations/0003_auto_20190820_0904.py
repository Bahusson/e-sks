# Generated by Django 2.2.4 on 2019-08-20 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_hotel',
            field=models.BooleanField(default=False, verbose_name='hotel'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_translator',
            field=models.BooleanField(default=False, verbose_name='translator'),
        ),
        migrations.AddField(
            model_name='user',
            name='role_council',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'User'), (2, 'Council'), (3, 'Council Admin'), (4, 'Superuser')], null=True),
        ),
    ]
