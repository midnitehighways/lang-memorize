# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0011_word_user2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='word',
            name='user',
        ),
        migrations.RemoveField(
            model_name='word',
            name='user2',
        ),
        migrations.AddField(
            model_name='word',
            name='userid',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
