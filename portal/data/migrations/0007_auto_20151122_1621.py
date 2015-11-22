# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_remove_orgs_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='latitude',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='orgs',
            name='longitude',
            field=models.CharField(max_length=35),
        ),
    ]
