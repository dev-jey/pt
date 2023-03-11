# Generated by Django 3.2.18 on 2023-03-11 13:45

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20230218_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=1000)),
                ('description', tinymce.models.HTMLField()),
                ('logo_url', models.CharField(default='', max_length=1000)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
