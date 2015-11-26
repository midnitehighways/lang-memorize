# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0002_auto_20151116_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example',
            name='en',
            field=models.TextField(default='-', max_length=100),
        ),
        migrations.AlterField(
            model_name='example',
            name='fi',
            field=models.TextField(default='-', max_length=100),
        ),
    ]
