# Generated by Django 2.2.4 on 2019-08-23 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0007_auto_20190823_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicationformfields',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='userdocs'),
        ),
    ]
