# Generated by Django 2.2.4 on 2019-09-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0008_auto_20190916_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageskin',
            name='filesideimage',
            field=models.ImageField(blank=True, null=True, upload_to='skins'),
        ),
        migrations.AddField(
            model_name='pageskin',
            name='infoimagedefault',
            field=models.ImageField(blank=True, null=True, upload_to='skins'),
        ),
        migrations.AddField(
            model_name='pageskin',
            name='infosideimage',
            field=models.ImageField(blank=True, null=True, upload_to='skins'),
        ),
        migrations.AlterField(
            model_name='pageskin',
            name='blogimagedefault',
            field=models.ImageField(blank=True, null=True, upload_to='skins'),
        ),
    ]
