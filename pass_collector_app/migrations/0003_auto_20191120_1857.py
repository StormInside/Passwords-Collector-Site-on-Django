# Generated by Django 2.2.3 on 2019-11-20 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pass_collector_app', '0002_auto_20191120_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passwords',
            old_name='user_id',
            new_name='user',
        ),
    ]
