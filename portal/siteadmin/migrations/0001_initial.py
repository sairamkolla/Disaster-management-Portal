# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acceptance_Disaster_Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_accepted', models.IntegerField(default=0)),
                ('seen', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Disaster_Approval_Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_visited', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Disaster_Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_of_sos_received', models.IntegerField(default=0)),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
                ('is_confirmed', models.BooleanField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('disaster_code', models.CharField(max_length=2)),
                ('disaster_name', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=200)),
                ('no_people_affected', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Sos_Reports',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disaster_code', models.CharField(max_length=2)),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
                ('sos_timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_disaster', models.BooleanField(default=0)),
                ('disaster_id', models.ForeignKey(blank=True, to='siteadmin.Disaster_Description', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='disaster_approval_admin',
            name='disaster_id',
            field=models.ForeignKey(to='siteadmin.Disaster_Description'),
        ),
        migrations.AddField(
            model_name='acceptance_disaster_org',
            name='disaster_id',
            field=models.ForeignKey(to='siteadmin.Disaster_Description'),
        ),
    ]
