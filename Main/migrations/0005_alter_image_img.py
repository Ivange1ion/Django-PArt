# Generated by Django 4.2.5 on 2024-03-05 08:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_alter_image_teg1_alter_image_teg2_alter_image_teg3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.ImageField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['pdf', 'doc', 'svg'])]),
        ),
    ]