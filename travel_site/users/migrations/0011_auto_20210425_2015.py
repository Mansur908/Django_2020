# Generated by Django 3.1.6 on 2021-04-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210409_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='picture',
        ),
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateTimeField(default=None),
        ),
        migrations.DeleteModel(
            name='Favorites',
        ),
    ]
