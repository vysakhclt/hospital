# Generated by Django 3.2.4 on 2021-06-25 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('img', models.ImageField(upload_to='blog')),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('qualification', models.CharField(max_length=150)),
                ('photo', models.ImageField(upload_to='doctor')),
                ('detail', models.TextField()),
            ],
            options={
                'verbose_name': 'doctor',
                'verbose_name_plural': 'doctors',
                'ordering': ('name',),
            },
        ),
    ]
