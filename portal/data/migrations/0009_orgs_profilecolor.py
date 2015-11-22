# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_auto_20151122_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgs',
            name='profilecolor',
            field=models.CharField(default=b'#030303', max_length=7),
        ),
    ]
