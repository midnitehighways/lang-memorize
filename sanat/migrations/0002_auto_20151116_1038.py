# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sanat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('fi', models.TextField(max_length=100)),
                ('en', models.TextField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='word',
            name='en',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='word',
            name='fi',
            field=models.TextField(max_length=50),
        ),
        migrations.AddField(
            model_name='example',
            name='word',
            field=models.ForeignKey(to='sanat.Word'),
        ),
    ]
