# Generated by Django 4.2.11 on 2024-04-01 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_pattern_description_alter_pattern_gauge_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pattern',
            name='instructions',
        ),
    ]
