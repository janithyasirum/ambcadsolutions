# Generated by Django 5.1.3 on 2024-11-12 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anushka', '0006_cnccutting_link_furnitureandtoys_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drawing2d3d',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='drawing2d3d',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='drawing2d3d',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]