# Generated by Django 5.0.6 on 2024-10-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_cours_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cours',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
