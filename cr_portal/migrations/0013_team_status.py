# Generated by Django 3.2.7 on 2022-06-27 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr_portal', '0012_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='status',
            field=models.BooleanField(default='False'),
        ),
    ]
