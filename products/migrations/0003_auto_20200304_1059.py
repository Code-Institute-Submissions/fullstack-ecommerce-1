# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-04 10:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='product_details',
            new_name='product_image',
        ),
    ]
