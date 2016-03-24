# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0017_auto_20160321_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='tyyppi',
            field=models.TextField(choices=[('V', 'Verb'), ('S', 'Substantive'), ('A', 'Adjective'), ('D', 'Adverb'), ('M', 'Else'), ('E', 'Not mentioned')], default='E'),
        ),
    ]
