# Generated by Django 4.1.4 on 2022-12-16 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(upload_to='Test/product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.CharField(max_length=255),
        ),
    ]
