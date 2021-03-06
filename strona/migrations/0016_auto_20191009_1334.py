# Generated by Django 2.2.4 on 2019-10-09 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0015_pageskin_welcomebanner_small'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileserve',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='fileserve',
            name='file_de',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='fileserve',
            name='file_en',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='fileserve',
            name='file_es',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='fileserve',
            name='file_fr',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='fileserve',
            name='file_hi',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='fileserve',
            name='file_pl',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='fileserve',
            name='file_ru',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
        migrations.AlterField(
            model_name='fileserve',
            name='file_uk',
            field=models.FileField(blank=True, null=True, upload_to='docs'),
        ),
    ]
