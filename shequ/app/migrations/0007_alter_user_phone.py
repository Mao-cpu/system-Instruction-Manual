# Generated by Django 4.0.5 on 2022-06-27 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_user_delete_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
