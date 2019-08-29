# Generated by Django 2.2.4 on 2019-08-23 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0004_auto_20190823_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='formitems',
            name='assign_again_de',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assign_again_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assign_again_es',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assign_again_fr',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assign_again_hi',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assign_again_pl',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assign_again_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assign_again_uk',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assigned_to_de',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assigned_to_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assigned_to_es',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assigned_to_fr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assigned_to_hi',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assigned_to_pl',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assigned_to_ru',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='assigned_to_uk',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='data_correct_de',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='data_correct_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='data_correct_es',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='data_correct_fr',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='data_correct_hi',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='data_correct_pl',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='data_correct_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='formitems',
            name='data_correct_uk',
            field=models.CharField(max_length=250, null=True),
        ),
    ]