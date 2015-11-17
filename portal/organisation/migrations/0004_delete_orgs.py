# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0003_auto_20151117_0652'),
        ('siteadmin', '0005_auto_20151117_0652'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orgs',
        ),
    ]
