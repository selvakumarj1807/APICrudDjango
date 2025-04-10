# Generated by Django 3.1.12 on 2025-04-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentEnquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('currently_working', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
