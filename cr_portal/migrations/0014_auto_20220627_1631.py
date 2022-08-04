# Generated by Django 3.2.7 on 2022-06-27 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_portal', '0013_team_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='crid1',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='team',
            name='crid2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='team',
            name='crid3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='team',
            name='crid4',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='leader',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='member2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='member3',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='member4',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='team',
            name='teamname',
            field=models.CharField(default='', max_length=200),
        ),
    ]