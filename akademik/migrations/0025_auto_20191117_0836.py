# Generated by Django 2.2.4 on 2019-11-17 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0024_auto_20191016_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='admintexttools',
            name='searchme',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='searchme_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='searchme_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='searchme_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='searchme_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='searchme_hi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='searchme_pl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='searchme_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='searchme_uk',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
