# Generated by Django 3.2.9 on 2021-11-21 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wendy_gallery', '0002_auto_20211121_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='details',
            field=models.TextField(default='wendys closet', help_text='Full product details'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='summery',
            field=models.TextField(default='Wendys closet', verbose_name='product summary description'),
        ),
    ]
