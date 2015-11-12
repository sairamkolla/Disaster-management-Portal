# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0003_disaster_description_is_viewed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disaster_Proposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_of_sos_received', models.IntegerField(default=0)),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('disaster_code', models.CharField(max_length=2)),
                ('disaster_name', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=200)),
                ('no_people_affected', models.IntegerField(default=0)),
                ('is_viewed', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='disaster_description',
            name='is_confirmed',
        ),
        migrations.RemoveField(
            model_name='disaster_description',
            name='is_viewed',
        ),
    ]
