# Generated by Django 5.1.3 on 2024-11-08 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anushka', '0003_metalstrture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furnitureandtoys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
    ]