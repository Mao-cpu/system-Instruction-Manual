# Generated by Django 4.0.5 on 2022-06-28 15:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_blog_nocheck_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('path', models.CharField(max_length=100)),
                ('upload_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]