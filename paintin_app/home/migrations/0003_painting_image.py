# Generated by Django 4.2.1 on 2023-07-17 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_painting'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
