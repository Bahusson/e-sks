# Generated by Django 2.2.4 on 2019-08-15 04:03

from django.db import migrations, models
import rekruter.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=50, null=True)),
                ('login_pl', models.CharField(max_length=50, null=True)),
                ('login_en', models.CharField(max_length=50, null=True)),
                ('login_de', models.CharField(max_length=50, null=True)),
                ('login_fr', models.CharField(max_length=50, null=True)),
                ('login_ru', models.CharField(max_length=50, null=True)),
                ('login_uk', models.CharField(max_length=50, null=True)),
                ('login_es', models.CharField(max_length=50, null=True)),
                ('login_hi', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
                ('password_pl', models.CharField(max_length=50, null=True)),
                ('password_en', models.CharField(max_length=50, null=True)),
                ('password_de', models.CharField(max_length=50, null=True)),
                ('password_fr', models.CharField(max_length=50, null=True)),
                ('password_ru', models.CharField(max_length=50, null=True)),
                ('password_uk', models.CharField(max_length=50, null=True)),
                ('password_es', models.CharField(max_length=50, null=True)),
                ('password_hi', models.CharField(max_length=50, null=True)),
                ('re_password', models.CharField(max_length=50, null=True)),
                ('re_password_pl', models.CharField(max_length=50, null=True)),
                ('re_password_en', models.CharField(max_length=50, null=True)),
                ('re_password_de', models.CharField(max_length=50, null=True)),
                ('re_password_fr', models.CharField(max_length=50, null=True)),
                ('re_password_ru', models.CharField(max_length=50, null=True)),
                ('re_password_uk', models.CharField(max_length=50, null=True)),
                ('re_password_es', models.CharField(max_length=50, null=True)),
                ('re_password_hi', models.CharField(max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('name_pl', models.CharField(max_length=50, null=True)),
                ('name_en', models.CharField(max_length=50, null=True)),
                ('name_de', models.CharField(max_length=50, null=True)),
                ('name_fr', models.CharField(max_length=50, null=True)),
                ('name_ru', models.CharField(max_length=50, null=True)),
                ('name_uk', models.CharField(max_length=50, null=True)),
                ('name_es', models.CharField(max_length=50, null=True)),
                ('name_hi', models.CharField(max_length=50, null=True)),
                ('surname', models.CharField(max_length=50, null=True)),
                ('surname_pl', models.CharField(max_length=50, null=True)),
                ('surname_en', models.CharField(max_length=50, null=True)),
                ('surname_de', models.CharField(max_length=50, null=True)),
                ('surname_fr', models.CharField(max_length=50, null=True)),
                ('surname_ru', models.CharField(max_length=50, null=True)),
                ('surname_uk', models.CharField(max_length=50, null=True)),
                ('surname_es', models.CharField(max_length=50, null=True)),
                ('surname_hi', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('email_pl', models.CharField(max_length=50, null=True)),
                ('email_en', models.CharField(max_length=50, null=True)),
                ('email_de', models.CharField(max_length=50, null=True)),
                ('email_fr', models.CharField(max_length=50, null=True)),
                ('email_ru', models.CharField(max_length=50, null=True)),
                ('email_uk', models.CharField(max_length=50, null=True)),
                ('email_es', models.CharField(max_length=50, null=True)),
                ('email_hi', models.CharField(max_length=50, null=True)),
                ('register', models.CharField(max_length=50, null=True)),
                ('register_pl', models.CharField(max_length=50, null=True)),
                ('register_en', models.CharField(max_length=50, null=True)),
                ('register_de', models.CharField(max_length=50, null=True)),
                ('register_fr', models.CharField(max_length=50, null=True)),
                ('register_ru', models.CharField(max_length=50, null=True)),
                ('register_uk', models.CharField(max_length=50, null=True)),
                ('register_es', models.CharField(max_length=50, null=True)),
                ('register_hi', models.CharField(max_length=50, null=True)),
                ('admin_panel', models.CharField(max_length=50, null=True)),
                ('admin_panel_pl', models.CharField(max_length=50, null=True)),
                ('admin_panel_en', models.CharField(max_length=50, null=True)),
                ('admin_panel_de', models.CharField(max_length=50, null=True)),
                ('admin_panel_fr', models.CharField(max_length=50, null=True)),
                ('admin_panel_ru', models.CharField(max_length=50, null=True)),
                ('admin_panel_uk', models.CharField(max_length=50, null=True)),
                ('admin_panel_es', models.CharField(max_length=50, null=True)),
                ('admin_panel_hi', models.CharField(max_length=50, null=True)),
                ('back', models.CharField(max_length=50, null=True)),
                ('back_pl', models.CharField(max_length=50, null=True)),
                ('back_en', models.CharField(max_length=50, null=True)),
                ('back_de', models.CharField(max_length=50, null=True)),
                ('back_fr', models.CharField(max_length=50, null=True)),
                ('back_ru', models.CharField(max_length=50, null=True)),
                ('back_uk', models.CharField(max_length=50, null=True)),
                ('back_es', models.CharField(max_length=50, null=True)),
                ('back_hi', models.CharField(max_length=50, null=True)),
                ('action', models.CharField(max_length=50, null=True)),
                ('action_pl', models.CharField(max_length=50, null=True)),
                ('action_en', models.CharField(max_length=50, null=True)),
                ('action_de', models.CharField(max_length=50, null=True)),
                ('action_fr', models.CharField(max_length=50, null=True)),
                ('action_ru', models.CharField(max_length=50, null=True)),
                ('action_uk', models.CharField(max_length=50, null=True)),
                ('action_es', models.CharField(max_length=50, null=True)),
                ('action_hi', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuarterClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_local', models.CharField(max_length=50, null=True)),
                ('stud_local_pl', models.CharField(max_length=50, null=True)),
                ('stud_local_en', models.CharField(max_length=50, null=True)),
                ('stud_local_de', models.CharField(max_length=50, null=True)),
                ('stud_local_fr', models.CharField(max_length=50, null=True)),
                ('stud_local_ru', models.CharField(max_length=50, null=True)),
                ('stud_local_uk', models.CharField(max_length=50, null=True)),
                ('stud_local_es', models.CharField(max_length=50, null=True)),
                ('stud_local_hi', models.CharField(max_length=50, null=True)),
                ('stud_foreign', models.CharField(max_length=50, null=True)),
                ('stud_foreign_pl', models.CharField(max_length=50, null=True)),
                ('stud_foreign_en', models.CharField(max_length=50, null=True)),
                ('stud_foreign_de', models.CharField(max_length=50, null=True)),
                ('stud_foreign_fr', models.CharField(max_length=50, null=True)),
                ('stud_foreign_ru', models.CharField(max_length=50, null=True)),
                ('stud_foreign_uk', models.CharField(max_length=50, null=True)),
                ('stud_foreign_es', models.CharField(max_length=50, null=True)),
                ('stud_foreign_hi', models.CharField(max_length=50, null=True)),
                ('phd', models.CharField(max_length=50, null=True)),
                ('phd_pl', models.CharField(max_length=50, null=True)),
                ('phd_en', models.CharField(max_length=50, null=True)),
                ('phd_de', models.CharField(max_length=50, null=True)),
                ('phd_fr', models.CharField(max_length=50, null=True)),
                ('phd_ru', models.CharField(max_length=50, null=True)),
                ('phd_uk', models.CharField(max_length=50, null=True)),
                ('phd_es', models.CharField(max_length=50, null=True)),
                ('phd_hi', models.CharField(max_length=50, null=True)),
                ('bank', models.CharField(max_length=50, null=True)),
                ('bank_pl', models.CharField(max_length=50, null=True)),
                ('bank_en', models.CharField(max_length=50, null=True)),
                ('bank_de', models.CharField(max_length=50, null=True)),
                ('bank_fr', models.CharField(max_length=50, null=True)),
                ('bank_ru', models.CharField(max_length=50, null=True)),
                ('bank_uk', models.CharField(max_length=50, null=True)),
                ('bank_es', models.CharField(max_length=50, null=True)),
                ('bank_hi', models.CharField(max_length=50, null=True)),
                ('new1', models.CharField(max_length=50, null=True)),
                ('new1_pl', models.CharField(max_length=50, null=True)),
                ('new1_en', models.CharField(max_length=50, null=True)),
                ('new1_de', models.CharField(max_length=50, null=True)),
                ('new1_fr', models.CharField(max_length=50, null=True)),
                ('new1_ru', models.CharField(max_length=50, null=True)),
                ('new1_uk', models.CharField(max_length=50, null=True)),
                ('new1_es', models.CharField(max_length=50, null=True)),
                ('new1_hi', models.CharField(max_length=50, null=True)),
                ('new23', models.CharField(max_length=50, null=True)),
                ('new23_pl', models.CharField(max_length=50, null=True)),
                ('new23_en', models.CharField(max_length=50, null=True)),
                ('new23_de', models.CharField(max_length=50, null=True)),
                ('new23_fr', models.CharField(max_length=50, null=True)),
                ('new23_ru', models.CharField(max_length=50, null=True)),
                ('new23_uk', models.CharField(max_length=50, null=True)),
                ('new23_es', models.CharField(max_length=50, null=True)),
                ('new23_hi', models.CharField(max_length=50, null=True)),
                ('new_foreign', models.CharField(max_length=50, null=True)),
                ('new_foreign_pl', models.CharField(max_length=50, null=True)),
                ('new_foreign_en', models.CharField(max_length=50, null=True)),
                ('new_foreign_de', models.CharField(max_length=50, null=True)),
                ('new_foreign_fr', models.CharField(max_length=50, null=True)),
                ('new_foreign_ru', models.CharField(max_length=50, null=True)),
                ('new_foreign_uk', models.CharField(max_length=50, null=True)),
                ('new_foreign_es', models.CharField(max_length=50, null=True)),
                ('new_foreign_hi', models.CharField(max_length=50, null=True)),
                ('erasmus', models.CharField(max_length=50, null=True)),
                ('erasmus_pl', models.CharField(max_length=50, null=True)),
                ('erasmus_en', models.CharField(max_length=50, null=True)),
                ('erasmus_de', models.CharField(max_length=50, null=True)),
                ('erasmus_fr', models.CharField(max_length=50, null=True)),
                ('erasmus_ru', models.CharField(max_length=50, null=True)),
                ('erasmus_uk', models.CharField(max_length=50, null=True)),
                ('erasmus_es', models.CharField(max_length=50, null=True)),
                ('erasmus_hi', models.CharField(max_length=50, null=True)),
                ('bilateral', models.CharField(max_length=50, null=True)),
                ('bilateral_pl', models.CharField(max_length=50, null=True)),
                ('bilateral_en', models.CharField(max_length=50, null=True)),
                ('bilateral_de', models.CharField(max_length=50, null=True)),
                ('bilateral_fr', models.CharField(max_length=50, null=True)),
                ('bilateral_ru', models.CharField(max_length=50, null=True)),
                ('bilateral_uk', models.CharField(max_length=50, null=True)),
                ('bilateral_es', models.CharField(max_length=50, null=True)),
                ('bilateral_hi', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.CharField(max_length=500)),
                ('intro_pl', models.CharField(max_length=500, null=True)),
                ('intro_en', models.CharField(max_length=500, null=True)),
                ('intro_de', models.CharField(max_length=500, null=True)),
                ('intro_fr', models.CharField(max_length=500, null=True)),
                ('intro_ru', models.CharField(max_length=500, null=True)),
                ('intro_uk', models.CharField(max_length=500, null=True)),
                ('intro_es', models.CharField(max_length=500, null=True)),
                ('intro_hi', models.CharField(max_length=500, null=True)),
                ('yes', models.CharField(max_length=50, null=True)),
                ('yes_pl', models.CharField(max_length=50, null=True)),
                ('yes_en', models.CharField(max_length=50, null=True)),
                ('yes_de', models.CharField(max_length=50, null=True)),
                ('yes_fr', models.CharField(max_length=50, null=True)),
                ('yes_ru', models.CharField(max_length=50, null=True)),
                ('yes_uk', models.CharField(max_length=50, null=True)),
                ('yes_es', models.CharField(max_length=50, null=True)),
                ('yes_hi', models.CharField(max_length=50, null=True)),
                ('no', models.CharField(max_length=50, null=True)),
                ('no_pl', models.CharField(max_length=50, null=True)),
                ('no_en', models.CharField(max_length=50, null=True)),
                ('no_de', models.CharField(max_length=50, null=True)),
                ('no_fr', models.CharField(max_length=50, null=True)),
                ('no_ru', models.CharField(max_length=50, null=True)),
                ('no_uk', models.CharField(max_length=50, null=True)),
                ('no_es', models.CharField(max_length=50, null=True)),
                ('no_hi', models.CharField(max_length=50, null=True)),
                ('oswiadczenie', models.TextField()),
                ('oswiadczenie_pl', models.TextField(null=True)),
                ('oswiadczenie_en', models.TextField(null=True)),
                ('oswiadczenie_de', models.TextField(null=True)),
                ('oswiadczenie_fr', models.TextField(null=True)),
                ('oswiadczenie_ru', models.TextField(null=True)),
                ('oswiadczenie_uk', models.TextField(null=True)),
                ('oswiadczenie_es', models.TextField(null=True)),
                ('oswiadczenie_hi', models.TextField(null=True)),
                ('obywatelstwo', models.CharField(max_length=150)),
                ('obywatelstwo_pl', models.CharField(max_length=150, null=True)),
                ('obywatelstwo_en', models.CharField(max_length=150, null=True)),
                ('obywatelstwo_de', models.CharField(max_length=150, null=True)),
                ('obywatelstwo_fr', models.CharField(max_length=150, null=True)),
                ('obywatelstwo_ru', models.CharField(max_length=150, null=True)),
                ('obywatelstwo_uk', models.CharField(max_length=150, null=True)),
                ('obywatelstwo_es', models.CharField(max_length=150, null=True)),
                ('obywatelstwo_hi', models.CharField(max_length=150, null=True)),
                ('student', models.CharField(max_length=150)),
                ('student_pl', models.CharField(max_length=150, null=True)),
                ('student_en', models.CharField(max_length=150, null=True)),
                ('student_de', models.CharField(max_length=150, null=True)),
                ('student_fr', models.CharField(max_length=150, null=True)),
                ('student_ru', models.CharField(max_length=150, null=True)),
                ('student_uk', models.CharField(max_length=150, null=True)),
                ('student_es', models.CharField(max_length=150, null=True)),
                ('student_hi', models.CharField(max_length=150, null=True)),
                ('doktorant', models.CharField(max_length=150)),
                ('doktorant_pl', models.CharField(max_length=150, null=True)),
                ('doktorant_en', models.CharField(max_length=150, null=True)),
                ('doktorant_de', models.CharField(max_length=150, null=True)),
                ('doktorant_fr', models.CharField(max_length=150, null=True)),
                ('doktorant_ru', models.CharField(max_length=150, null=True)),
                ('doktorant_uk', models.CharField(max_length=150, null=True)),
                ('doktorant_es', models.CharField(max_length=150, null=True)),
                ('doktorant_hi', models.CharField(max_length=150, null=True)),
                ('zamiar', models.CharField(max_length=150)),
                ('zamiar_pl', models.CharField(max_length=150, null=True)),
                ('zamiar_en', models.CharField(max_length=150, null=True)),
                ('zamiar_de', models.CharField(max_length=150, null=True)),
                ('zamiar_fr', models.CharField(max_length=150, null=True)),
                ('zamiar_ru', models.CharField(max_length=150, null=True)),
                ('zamiar_uk', models.CharField(max_length=150, null=True)),
                ('zamiar_es', models.CharField(max_length=150, null=True)),
                ('zamiar_hi', models.CharField(max_length=150, null=True)),
                ('pierwszegosto', models.CharField(max_length=150)),
                ('pierwszegosto_pl', models.CharField(max_length=150, null=True)),
                ('pierwszegosto_en', models.CharField(max_length=150, null=True)),
                ('pierwszegosto_de', models.CharField(max_length=150, null=True)),
                ('pierwszegosto_fr', models.CharField(max_length=150, null=True)),
                ('pierwszegosto_ru', models.CharField(max_length=150, null=True)),
                ('pierwszegosto_uk', models.CharField(max_length=150, null=True)),
                ('pierwszegosto_es', models.CharField(max_length=150, null=True)),
                ('pierwszegosto_hi', models.CharField(max_length=150, null=True)),
                ('pelnywym', models.CharField(max_length=150)),
                ('pelnywym_pl', models.CharField(max_length=150, null=True)),
                ('pelnywym_en', models.CharField(max_length=150, null=True)),
                ('pelnywym_de', models.CharField(max_length=150, null=True)),
                ('pelnywym_fr', models.CharField(max_length=150, null=True)),
                ('pelnywym_ru', models.CharField(max_length=150, null=True)),
                ('pelnywym_uk', models.CharField(max_length=150, null=True)),
                ('pelnywym_es', models.CharField(max_length=150, null=True)),
                ('pelnywym_hi', models.CharField(max_length=150, null=True)),
                ('erasmus', models.CharField(max_length=150)),
                ('erasmus_pl', models.CharField(max_length=150, null=True)),
                ('erasmus_en', models.CharField(max_length=150, null=True)),
                ('erasmus_de', models.CharField(max_length=150, null=True)),
                ('erasmus_fr', models.CharField(max_length=150, null=True)),
                ('erasmus_ru', models.CharField(max_length=150, null=True)),
                ('erasmus_uk', models.CharField(max_length=150, null=True)),
                ('erasmus_es', models.CharField(max_length=150, null=True)),
                ('erasmus_hi', models.CharField(max_length=150, null=True)),
                ('buttondalej', models.CharField(max_length=100)),
                ('buttondalej_pl', models.CharField(max_length=100, null=True)),
                ('buttondalej_en', models.CharField(max_length=100, null=True)),
                ('buttondalej_de', models.CharField(max_length=100, null=True)),
                ('buttondalej_fr', models.CharField(max_length=100, null=True)),
                ('buttondalej_ru', models.CharField(max_length=100, null=True)),
                ('buttondalej_uk', models.CharField(max_length=100, null=True)),
                ('buttondalej_es', models.CharField(max_length=100, null=True)),
                ('buttondalej_hi', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('quarter', models.CharField(blank=True, max_length=2, verbose_name='quarter')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', rekruter.managers.UserManager()),
            ],
        ),
    ]
