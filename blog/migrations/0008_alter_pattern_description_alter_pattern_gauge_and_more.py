# Generated by Django 4.2.11 on 2024-04-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_pattern_gauge_alter_pattern_needle_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pattern',
            name='description',
            field=models.CharField(default='description', max_length=200),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='gauge',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='needle_size',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='pattern_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='yarn',
            field=models.CharField(default='yarn', max_length=50),
        ),
    ]
