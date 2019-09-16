# Generated by Django 2.2.4 on 2019-09-16 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0007_auto_20190915_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='formelement',
            name='blog',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formelement',
            name='blog_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='blog_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='blog_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='blog_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='blog_hi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='blog_pl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='blog_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='blog_uk',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='change',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formelement',
            name='change_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='change_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='change_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='change_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='change_hi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='change_pl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='change_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='change_uk',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='file',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formelement',
            name='file_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='file_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='file_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='file_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='file_hi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='file_pl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='file_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='file_uk',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='info',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formelement',
            name='info_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='info_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='info_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='info_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='info_hi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='info_pl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='info_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='info_uk',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='new',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formelement',
            name='new_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='new_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='new_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='new_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='new_hi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='new_pl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='new_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='formelement',
            name='new_uk',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
