# Generated by Django 3.2.4 on 2021-06-29 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_index_app', '0002_rename_img_blog_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('phone', models.TextField()),
                ('time_slot', models.DateTimeField()),
                ('department', models.TextField()),
                ('doctor', models.TextField()),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
                'ordering': ('patient_name',),
            },
        ),
    ]
