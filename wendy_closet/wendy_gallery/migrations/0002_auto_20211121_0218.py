# Generated by Django 3.2.9 on 2021-11-21 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wendy_gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='details',
            field=models.TextField(default=1, help_text='Full product details'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='gallery',
            name='summery',
            field=models.TextField(default=1, verbose_name='product summary description'),
            preserve_default=False,
        ),
    ]
