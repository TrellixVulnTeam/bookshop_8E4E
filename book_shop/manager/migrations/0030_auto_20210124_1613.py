# Generated by Django 3.1.5 on 2021-01-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0029_auto_20210124_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
