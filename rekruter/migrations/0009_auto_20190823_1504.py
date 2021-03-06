# Generated by Django 2.2.4 on 2019-08-23 15:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rekruter', '0008_applicationformfields_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuarterClassB',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('position', models.IntegerField()),
            ],
            options={
                'ordering': ['position', 'id'],
            },
        ),
        migrations.AlterModelOptions(
            name='applicationformfields',
            options={'ordering': ['owner', 'application_no']},
        ),
        migrations.RemoveField(
            model_name='applicationformfields',
            name='id',
        ),
        migrations.RemoveField(
            model_name='applicationformfields',
            name='name',
        ),
        migrations.AddField(
            model_name='applicationformfields',
            name='application_no',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
