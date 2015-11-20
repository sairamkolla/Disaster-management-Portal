# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20151120_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgs',
            name='profilepic',
        ),
    ]
