# Generated by Django 3.2.18 on 2023-03-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_about_upwork'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='industry',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
