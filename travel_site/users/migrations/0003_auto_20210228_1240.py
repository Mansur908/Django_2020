# Generated by Django 3.1.6 on 2021-02-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210228_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='person',
            name='picture',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]