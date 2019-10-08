# Generated by Django 2.2.4 on 2019-09-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0010_pageskin_welcomebanner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pageskin',
            options={'ordering': ['position']},
        ),
        migrations.AddField(
            model_name='pageskin',
            name='fileimagedefault',
            field=models.ImageField(blank=True, null=True, upload_to='skins'),
        ),
        migrations.AddField(
            model_name='pageskin',
            name='position',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pageskin',
            name='themetitle',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]