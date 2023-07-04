# Generated by Django 4.1 on 2023-06-30 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_portal', '0034_userprofile_proof2_userprofile_task2_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='proof3',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='proof4',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='task3_status',
            field=models.BooleanField(default='False'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='task4_status',
            field=models.BooleanField(default='False'),
        ),
    ]