# Generated by Django 2.2.4 on 2019-08-30 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0016_auto_20190830_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='album',
            field=models.CharField(blank=True, max_length=25, verbose_name='album'),
        ),
    ]
