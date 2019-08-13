# Generated by Django 2.2.4 on 2019-08-10 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strona', '0004_auto_20190809_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageitem',
            name='panel_staff',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_staff_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_staff_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_staff_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_staff_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_staff_hi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_staff_pl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_staff_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_staff_uk',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_user',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_user_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_user_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_user_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_user_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_user_hi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_user_pl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_user_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='pageitem',
            name='panel_user_uk',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='login',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='login_de',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='login_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='login_es',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='login_fr',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='login_hi',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='login_pl',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='login_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pageitem',
            name='login_uk',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
