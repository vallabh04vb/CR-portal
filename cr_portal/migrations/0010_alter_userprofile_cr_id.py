# Generated by Django 3.2.7 on 2022-06-27 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_portal', '0009_auto_20220626_0631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cr_id',
            field=models.CharField(default='', max_length=200),
        ),
    ]
