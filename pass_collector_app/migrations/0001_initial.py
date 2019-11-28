# Generated by Django 2.2.3 on 2019-11-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourse_name', models.CharField(max_length=200, verbose_name='sourse_name')),
                ('user_login', models.CharField(max_length=200, verbose_name='user_login')),
                ('user_password', models.CharField(max_length=200, verbose_name='user_passord')),
                ('password_creation_date', models.DateTimeField(null=True, verbose_name='password_creation_date')),
                ('link_to_site', models.CharField(max_length=200, verbose_name='link_to_site')),
                ('count_of_search', models.IntegerField(default=0, verbose_name='count_of_search')),
                ('count_of_copy', models.IntegerField(default=0, verbose_name='count_of_copy')),
            ],
        ),
    ]