# Generated by Django 4.0 on 2022-03-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lion', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
