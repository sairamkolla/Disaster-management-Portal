# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disasterproposal',
            name='reason',
            field=models.CharField(default=b'NotKnown', max_length=200),
        ),
    ]
