# Generated by Django 4.2.4 on 2023-10-30 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default_profile_picture.png', null=True, upload_to='profile_pics/'),
        ),
    ]
