# Generated by Django 2.2.4 on 2019-08-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0002_auto_20190822_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portalbaseitem',
            name='portal',
            field=models.CharField(choices=[('1', 'User'), ('2', 'Council'), ('3', 'Hotel'), ('4', 'Translator')], max_length=1, unique=True),
        ),
    ]