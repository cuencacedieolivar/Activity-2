# Generated by Django 5.1.2 on 2024-11-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_customuser_remove_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='plant_images/'),
        ),
    ]
