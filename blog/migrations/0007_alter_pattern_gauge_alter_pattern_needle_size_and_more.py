# Generated by Django 4.2.11 on 2024-04-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_pattern_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='gauge',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='needle_size',
            field=models.CharField(),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='pattern_name',
            field=models.CharField(unique=True),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='yarn',
            field=models.CharField(default='yarn'),
        ),
    ]
