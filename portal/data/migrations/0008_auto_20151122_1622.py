# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20151122_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disasterdescription',
            name='latitude',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='disasterdescription',
            name='longitude',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='disasterproposal',
            name='latitude',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='disasterproposal',
            name='longitude',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='sosreports',
            name='latitude',
            field=models.CharField(max_length=35),
        ),
        migrations.AlterField(
            model_name='sosreports',
            name='longitude',
            field=models.CharField(max_length=35),
        ),
    ]
