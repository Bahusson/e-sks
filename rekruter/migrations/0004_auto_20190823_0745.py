# Generated by Django 2.2.4 on 2019-08-23 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0003_auto_20190820_0904'),
    ]

    operations = [
        migrations.AddField(
            model_name='formitems',
            name='assign_again',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formitems',
            name='assigned_to',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='data_correct',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]