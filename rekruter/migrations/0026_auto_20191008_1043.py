# Generated by Django 2.2.4 on 2019-10-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0025_applicationformfields_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicationformfields',
            name='state',
        ),
        migrations.AddField(
            model_name='applicationformfields',
            name='status',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
