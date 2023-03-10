# Generated by Django 3.2.18 on 2023-02-18 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20230218_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=1055, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='sections',
            field=models.ManyToManyField(to='project.Section'),
        ),
        migrations.AddField(
            model_name='project',
            name='components',
            field=models.ManyToManyField(to='project.Component'),
        ),
    ]
