# Generated by Django 3.1.6 on 2021-04-25 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210425_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='place_to_go',
            name='text',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
