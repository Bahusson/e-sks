# Generated by Django 2.2.4 on 2019-09-16 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0021_auto_20190916_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationformfields',
            name='degree',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationformfields',
            name='duration',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationformfields',
            name='faculty',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationformfields',
            name='if_room_change',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationformfields',
            name='semester',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationformfields',
            name='sh_choice1',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationformfields',
            name='sh_choice2',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationformfields',
            name='sh_choice3',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationformfields',
            name='special_case_docs',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='applicationformfields',
            name='spouse_cohabitant',
            field=models.CharField(blank=True, default=1, max_length=2),
            preserve_default=False,
        ),
    ]