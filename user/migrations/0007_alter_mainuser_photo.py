# Generated by Django 3.2.9 on 2022-04-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_mainuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainuser',
            name='photo',
            field=models.FileField(default='profile.png', upload_to='users-avatar'),
        ),
    ]
