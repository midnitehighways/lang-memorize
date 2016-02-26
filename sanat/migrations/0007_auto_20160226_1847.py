# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0006_auto_20160226_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='tyyppi',
            field=models.TextField(default='E', choices=[('V', 'Verbi'), ('S', 'Substantiivi'), ('A', 'Adjektiivi'), ('D', 'Adverbi'), ('M', 'Jotain muuta'), ('E', 'Ei mitaan')]),
        ),
    ]
