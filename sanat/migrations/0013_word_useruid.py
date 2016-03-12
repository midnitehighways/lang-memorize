# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0012_auto_20160312_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='useruid',
            field=models.TextField(default='0'),
        ),
    ]
