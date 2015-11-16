# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fi', models.TextField(max_length=100)),
                ('en', models.TextField(max_length=200)),
                ('tyyppi', models.TextField(default='E', choices=[('V', 'Verbi'), ('S', 'Substantiivi'), ('E', 'Ei mitaan')])),
            ],
        ),
    ]
