# Generated by Django 3.2.23 on 2024-01-03 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
