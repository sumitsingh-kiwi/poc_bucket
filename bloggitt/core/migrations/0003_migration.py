# Generated by Django 3.1.2 on 2022-06-06 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_migration'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagdict',
            name='slug',
            field=models.SlugField(default='default', editable=False, max_length=200),
            preserve_default=False,
        ),
    ]
