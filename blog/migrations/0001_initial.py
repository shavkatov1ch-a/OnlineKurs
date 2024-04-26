# Generated by Django 5.0.4 on 2024-04-24 14:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_pay', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('profession', models.CharField(max_length=212)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='team')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=212)),
                ('last_name', models.CharField(max_length=212)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='images')),
                ('password', models.CharField(max_length=212)),
                ('region', models.CharField(max_length=212)),
            ],
        ),
        migrations.CreateModel(
            name='Video_Darslar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='video')),
                ('video', models.CharField(max_length=212)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Web_sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=212)),
                ('link', models.CharField(max_length=212)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=212)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.client')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.users'),
        ),
        migrations.AddField(
            model_name='client',
            name='video_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.video_darslar'),
        ),
        migrations.CreateModel(
            name='Web_images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='website')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.TimeField()),
                ('website_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.web_sites')),
            ],
        ),
    ]
