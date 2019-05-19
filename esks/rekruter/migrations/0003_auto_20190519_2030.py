# Generated by Django 2.1.7 on 2019-05-19 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0002_auto_20190410_1841'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sito',
            old_name='bilateral',
            new_name='pierwszegosto',
        ),
        migrations.RenameField(
            model_name='sito',
            old_name='bilateral_de',
            new_name='pierwszegosto_de',
        ),
        migrations.RenameField(
            model_name='sito',
            old_name='bilateral_en',
            new_name='pierwszegosto_en',
        ),
        migrations.RenameField(
            model_name='sito',
            old_name='bilateral_es',
            new_name='pierwszegosto_es',
        ),
        migrations.RenameField(
            model_name='sito',
            old_name='bilateral_fr',
            new_name='pierwszegosto_fr',
        ),
        migrations.RenameField(
            model_name='sito',
            old_name='bilateral_hi',
            new_name='pierwszegosto_hi',
        ),
        migrations.RenameField(
            model_name='sito',
            old_name='bilateral_pl',
            new_name='pierwszegosto_pl',
        ),
        migrations.RenameField(
            model_name='sito',
            old_name='bilateral_ru',
            new_name='pierwszegosto_ru',
        ),
        migrations.RenameField(
            model_name='sito',
            old_name='bilateral_uk',
            new_name='pierwszegosto_uk',
        ),
        migrations.RemoveField(
            model_name='sito',
            name='zadnezpow',
        ),
        migrations.RemoveField(
            model_name='sito',
            name='zadnezpow_de',
        ),
        migrations.RemoveField(
            model_name='sito',
            name='zadnezpow_en',
        ),
        migrations.RemoveField(
            model_name='sito',
            name='zadnezpow_es',
        ),
        migrations.RemoveField(
            model_name='sito',
            name='zadnezpow_fr',
        ),
        migrations.RemoveField(
            model_name='sito',
            name='zadnezpow_hi',
        ),
        migrations.RemoveField(
            model_name='sito',
            name='zadnezpow_pl',
        ),
        migrations.RemoveField(
            model_name='sito',
            name='zadnezpow_ru',
        ),
        migrations.RemoveField(
            model_name='sito',
            name='zadnezpow_uk',
        ),
        migrations.AddField(
            model_name='sito',
            name='no',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='no_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='no_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='no_es',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='no_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='no_hi',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='no_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='no_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='no_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='yes',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='yes_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='yes_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='yes_es',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='yes_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='yes_hi',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='yes_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='yes_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='sito',
            name='yes_uk',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
