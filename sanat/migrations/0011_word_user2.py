# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0010_word_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='user2',
            field=models.TextField(default='anonymous'),
        ),
    ]
