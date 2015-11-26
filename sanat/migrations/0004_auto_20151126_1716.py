# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0003_auto_20151125_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='en',
            field=models.TextField(max_length=100, default='-', blank=True),
        ),
        migrations.AlterField(
            model_name='example',
            name='fi',
            field=models.TextField(max_length=100, default='-', blank=True),
        ),
    ]
