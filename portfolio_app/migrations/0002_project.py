# Generated by Django 4.1.5 on 2023-02-11 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, upload_to='media/images/')),
                ('description', models.TextField()),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
