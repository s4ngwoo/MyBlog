# Generated by Django 4.2.3 on 2023-07-13 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0007_alter_series_options_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]
