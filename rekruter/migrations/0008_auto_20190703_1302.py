# Generated by Django 2.1.7 on 2019-07-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0007_auto_20190703_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='formitems',
            name='admin_panel_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='admin_panel_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='admin_panel_es',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='admin_panel_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='admin_panel_hi',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='admin_panel_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='admin_panel_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='admin_panel_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='back_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='back_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='back_es',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='back_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='back_hi',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='back_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='back_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='back_uk',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
