# Generated by Django 3.2.6 on 2021-08-18 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('logo_url', models.CharField(max_length=1024)),
                ('coach', models.CharField(max_length=10)),
                ('gm', models.CharField(max_length=10)),
                ('web_url', models.CharField(max_length=1024)),
            ],
        ),
    ]
