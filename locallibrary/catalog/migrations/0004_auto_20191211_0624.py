# Generated by Django 2.0.3 on 2019-12-11 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20191127_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='catalog/static'),
        ),
    ]
