# Generated by Django 4.0.4 on 2022-06-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backkkass', '0004_boost_type_core_auto_click_power_alter_boost_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'casual'), (1, 'auto')], default=0),
        ),
    ]