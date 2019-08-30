# Generated by Django 2.2.4 on 2019-08-30 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0014_auto_20190830_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='citizenship',
            field=models.CharField(blank=True, max_length=40, verbose_name='citizenship'),
        ),
        migrations.AddField(
            model_name='user',
            name='dowod',
            field=models.CharField(blank=True, max_length=20, verbose_name='dowod'),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'other'), (1, 'male'), (2, 'female')], null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='passport',
            field=models.CharField(blank=True, max_length=20, verbose_name='passport'),
        ),
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, verbose_name='telephone'),
        ),
    ]
