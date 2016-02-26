# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0005_auto_20151126_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='tyyppi',
            field=models.TextField(choices=[('V', 'Verbi'), ('S', 'Substantiivi'), ('A', 'Adjektiivi'), ('M', 'Jotain muuta'), ('E', 'Ei mitaan')], default='E'),
        ),
    ]
