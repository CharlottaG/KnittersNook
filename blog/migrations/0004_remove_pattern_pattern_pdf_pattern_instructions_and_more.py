# Generated by Django 4.2.11 on 2024-04-01 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pattern',
            name='pattern_pdf',
        ),
        migrations.AddField(
            model_name='pattern',
            name='instructions',
            field=models.TextField(default='instructions'),
        ),
        migrations.AlterField(
            model_name='pattern',
            name='description',
            field=models.CharField(default='description', max_length=50),
        ),
    ]
