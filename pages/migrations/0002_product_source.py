# Generated by Django 3.0.5 on 2020-08-18 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='source',
            field=models.URLField(default='google.com'),
        ),
    ]
