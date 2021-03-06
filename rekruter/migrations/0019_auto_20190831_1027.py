# Generated by Django 2.2.4 on 2019-08-31 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0018_auto_20190831_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specialcase',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='specialcase',
            name='name_de',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='specialcase',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='specialcase',
            name='name_es',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='specialcase',
            name='name_fr',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='specialcase',
            name='name_hi',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='specialcase',
            name='name_pl',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='specialcase',
            name='name_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='specialcase',
            name='name_uk',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
