# Generated by Django 4.2.6 on 2023-11-08 22:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
