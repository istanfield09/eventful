# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventful_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_id',
            field=models.PositiveSmallIntegerField(default=15),
            preserve_default=False,
        ),
    ]
