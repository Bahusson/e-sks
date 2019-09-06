# Generated by Django 2.2.4 on 2019-09-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akademik', '0012_auto_20190905_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='HousingPartyItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_titlePL', models.CharField(blank=True, max_length=200)),
                ('party_titlePL_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titlePL_en', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titlePL_de', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titlePL_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titlePL_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titlePL_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titlePL_es', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titlePL_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titleEN', models.CharField(blank=True, max_length=200)),
                ('party_titleEN_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titleEN_en', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titleEN_de', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titleEN_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titleEN_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titleEN_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titleEN_es', models.CharField(blank=True, max_length=200, null=True)),
                ('party_titleEN_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('choose_party', models.CharField(blank=True, max_length=200)),
                ('choose_party_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('choose_party_en', models.CharField(blank=True, max_length=200, null=True)),
                ('choose_party_de', models.CharField(blank=True, max_length=200, null=True)),
                ('choose_party_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('choose_party_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('choose_party_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('choose_party_es', models.CharField(blank=True, max_length=200, null=True)),
                ('choose_party_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('time_start', models.CharField(blank=True, max_length=200)),
                ('time_start_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('time_start_en', models.CharField(blank=True, max_length=200, null=True)),
                ('time_start_de', models.CharField(blank=True, max_length=200, null=True)),
                ('time_start_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('time_start_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('time_start_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('time_start_es', models.CharField(blank=True, max_length=200, null=True)),
                ('time_start_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('time_end', models.CharField(blank=True, max_length=200)),
                ('time_end_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('time_end_en', models.CharField(blank=True, max_length=200, null=True)),
                ('time_end_de', models.CharField(blank=True, max_length=200, null=True)),
                ('time_end_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('time_end_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('time_end_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('time_end_es', models.CharField(blank=True, max_length=200, null=True)),
                ('time_end_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('commentPL', models.CharField(blank=True, max_length=200)),
                ('commentPL_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('commentPL_en', models.CharField(blank=True, max_length=200, null=True)),
                ('commentPL_de', models.CharField(blank=True, max_length=200, null=True)),
                ('commentPL_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('commentPL_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('commentPL_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('commentPL_es', models.CharField(blank=True, max_length=200, null=True)),
                ('commentPL_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('commentEN', models.CharField(blank=True, max_length=200)),
                ('commentEN_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('commentEN_en', models.CharField(blank=True, max_length=200, null=True)),
                ('commentEN_de', models.CharField(blank=True, max_length=200, null=True)),
                ('commentEN_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('commentEN_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('commentEN_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('commentEN_es', models.CharField(blank=True, max_length=200, null=True)),
                ('commentEN_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('announcePL', models.CharField(blank=True, max_length=200)),
                ('announcePL_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('announcePL_en', models.CharField(blank=True, max_length=200, null=True)),
                ('announcePL_de', models.CharField(blank=True, max_length=200, null=True)),
                ('announcePL_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('announcePL_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('announcePL_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('announcePL_es', models.CharField(blank=True, max_length=200, null=True)),
                ('announcePL_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('announceEN', models.CharField(blank=True, max_length=200)),
                ('announceEN_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('announceEN_en', models.CharField(blank=True, max_length=200, null=True)),
                ('announceEN_de', models.CharField(blank=True, max_length=200, null=True)),
                ('announceEN_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('announceEN_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('announceEN_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('announceEN_es', models.CharField(blank=True, max_length=200, null=True)),
                ('announceEN_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('tick_form', models.CharField(blank=True, max_length=200)),
                ('tick_form_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('tick_form_en', models.CharField(blank=True, max_length=200, null=True)),
                ('tick_form_de', models.CharField(blank=True, max_length=200, null=True)),
                ('tick_form_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('tick_form_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('tick_form_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('tick_form_es', models.CharField(blank=True, max_length=200, null=True)),
                ('tick_form_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('p_from', models.CharField(blank=True, max_length=200)),
                ('p_from_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('p_from_en', models.CharField(blank=True, max_length=200, null=True)),
                ('p_from_de', models.CharField(blank=True, max_length=200, null=True)),
                ('p_from_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('p_from_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('p_from_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('p_from_es', models.CharField(blank=True, max_length=200, null=True)),
                ('p_from_hi', models.CharField(blank=True, max_length=200, null=True)),
                ('p_to', models.CharField(blank=True, max_length=200)),
                ('p_to_pl', models.CharField(blank=True, max_length=200, null=True)),
                ('p_to_en', models.CharField(blank=True, max_length=200, null=True)),
                ('p_to_de', models.CharField(blank=True, max_length=200, null=True)),
                ('p_to_fr', models.CharField(blank=True, max_length=200, null=True)),
                ('p_to_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('p_to_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('p_to_es', models.CharField(blank=True, max_length=200, null=True)),
                ('p_to_hi', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
