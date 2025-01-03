# Generated by Django 5.1.3 on 2024-11-13 03:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anushka', '0015_rename_image_sheetmetal_image1_sheetmetal_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metalstrture',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='metalstrture',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='img_profiles'),
        ),
        migrations.AddField(
            model_name='metalstrture',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='img_profiles'),
        ),
        migrations.AddField(
            model_name='metalstrture',
            name='link',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator]),
        ),
        migrations.AlterField(
            model_name='metalstrture',
            name='caption',
            field=models.CharField(max_length=70),
        ),
    ]
