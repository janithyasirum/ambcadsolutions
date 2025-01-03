# Generated by Django 5.1.3 on 2024-11-09 06:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anushka', '0005_drawing2d3d_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='cnccutting',
            name='link',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator]),
        ),
        migrations.AddField(
            model_name='furnitureandtoys',
            name='link',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator]),
        ),
        migrations.AddField(
            model_name='lasercutting',
            name='link',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator]),
        ),
        migrations.AddField(
            model_name='metalstrture',
            name='link',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator]),
        ),
        migrations.AddField(
            model_name='printing3d',
            name='link',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator]),
        ),
        migrations.AddField(
            model_name='productrendering',
            name='link',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator]),
        ),
        migrations.AddField(
            model_name='sheetmetal',
            name='link',
            field=models.URLField(blank=True, validators=[django.core.validators.URLValidator]),
        ),
    ]
