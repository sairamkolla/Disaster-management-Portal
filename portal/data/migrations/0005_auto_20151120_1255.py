# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20151119_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='profilepic',
            field=models.ImageField(upload_to=b'/home/sairam/sairam/sem3/SSAD/project/Disaster-management-Portal/portal/static/organisation/images/', null=True, verbose_name=b'label'),
        ),
    ]
