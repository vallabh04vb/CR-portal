# Generated by Django 3.2.7 on 2022-06-24 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_portal', '0005_alter_leaderboard_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='points',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
