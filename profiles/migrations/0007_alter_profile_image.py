# Generated by Django 4.2.15 on 2024-09-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../blank_profile_image_mlzrkw', upload_to='images/'),
        ),
    ]