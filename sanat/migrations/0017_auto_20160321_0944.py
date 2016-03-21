# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0016_auto_20160321_0930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='word',
            name='userid',
        ),
        migrations.RemoveField(
            model_name='word',
            name='useruid',
        ),
        migrations.AddField(
            model_name='word',
            name='show_in_common',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
