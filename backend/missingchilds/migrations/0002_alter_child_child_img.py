# Generated by Django 3.2.15 on 2022-09-27 05:44

import backend.common
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missingchilds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='child_img',
            field=models.ImageField(null=True, upload_to=backend.common.image_upload_path),
        ),
    ]