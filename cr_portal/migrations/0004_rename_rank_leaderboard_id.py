# Generated by Django 3.2.7 on 2022-06-24 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cr_portal', '0003_leaderboard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaderboard',
            old_name='rank',
            new_name='id',
        ),
    ]
