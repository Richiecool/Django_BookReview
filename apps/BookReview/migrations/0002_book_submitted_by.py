# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-10-13 03:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookReview', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='submitted_by',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='books_submitted', to='BookReview.User'),
            preserve_default=False,
        ),
    ]
