# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org_head', models.CharField(max_length=100)),
                ('org_strength', models.IntegerField(default=0)),
                ('name_of_org', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=100, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
    ]
