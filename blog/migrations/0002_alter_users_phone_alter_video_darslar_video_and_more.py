# Generated by Django 5.0.4 on 2024-04-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phone',
            field=models.CharField(max_length=212),
        ),
        migrations.AlterField(
            model_name='video_darslar',
            name='video',
            field=models.FileField(upload_to='video'),
        ),
        migrations.AlterField(
            model_name='web_sites',
            name='price',
            field=models.CharField(max_length=212),
        ),
    ]
