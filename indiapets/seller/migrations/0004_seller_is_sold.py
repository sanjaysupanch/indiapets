# Generated by Django 3.0.3 on 2020-07-24 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_merge_20200724_0512'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='is_sold',
            field=models.BooleanField(default=False),
        ),
    ]
