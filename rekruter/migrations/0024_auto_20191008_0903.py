# Generated by Django 2.2.4 on 2019-10-08 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0023_auto_20191008_0855'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='applicationformfields',
            options={'ordering': ['-timeapplied', 'owner']},
        ),
    ]