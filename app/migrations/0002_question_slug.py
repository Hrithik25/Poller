# Generated by Django 3.1.5 on 2021-04-16 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='slug',
            field=models.SlugField(default='question'),
            preserve_default=False,
        ),
    ]
