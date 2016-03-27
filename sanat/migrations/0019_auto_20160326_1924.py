# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0018_auto_20160324_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='tyyppi',
        ),
        migrations.AddField(
            model_name='word',
            name='word_type',
            field=models.TextField(default='E', choices=[('V', 'Verb'), ('S', 'Substantive'), ('A', 'Adjective'), ('D', 'Adverb'), ('M', 'Other'), ('E', 'Not mentioned')]),
        ),
    ]
