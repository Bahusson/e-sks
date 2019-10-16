# Generated by Django 2.2.4 on 2019-10-16 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0021_admintexttools_applicationlistitems_userlistitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='admintexttools',
            name='non_assigned',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='non_assigned_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='non_assigned_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='non_assigned_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='non_assigned_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='non_assigned_hi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='non_assigned_pl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='non_assigned_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='admintexttools',
            name='non_assigned_uk',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
