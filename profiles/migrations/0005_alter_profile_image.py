# Generated by Django 4.2.15 on 2024-09-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='https://res-console.cloudinary.com/dxfpqnmtu/thumbnails/v1/image/upload/v1723028139/YmxhbmtfcHJvZmlsZV9pbWFnZV9tbHpya3c=/drilldown', upload_to='images/'),
        ),
    ]