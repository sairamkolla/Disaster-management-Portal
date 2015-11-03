# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orgs',
            name='user',
        ),
        migrations.AddField(
            model_name='orgs',
            name='userid',
            field=models.IntegerField(default=0),
        ),
    ]
