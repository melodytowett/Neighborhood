# Generated by Django 4.0.4 on 2022-04-15 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resident', '0005_neighborhood_image_hood'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]