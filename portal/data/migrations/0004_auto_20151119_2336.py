# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_orgs_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orgs',
            name='profilepic',
            field=models.ImageField(upload_to=b'/home/sairam/sairam/sem3/SSAD/project/Disaster-management-Portal/portal/static/media/', null=True, verbose_name=b'label'),
        ),
    ]
