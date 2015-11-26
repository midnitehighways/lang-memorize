# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0004_auto_20151126_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='en',
            field=models.TextField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='example',
            name='fi',
            field=models.TextField(default='', max_length=100),
        ),
    ]
