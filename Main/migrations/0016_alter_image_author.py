# Generated by Django 4.2.5 on 2024-05-29 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0015_alter_image_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
