# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address_Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_name', models.CharField(max_length=50)),
                ('state_name', models.CharField(max_length=20)),
                ('door_number', models.CharField(max_length=10)),
                ('city_name', models.CharField(max_length=20)),
                ('pincode', models.CharField(max_length=6)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Mails_Orgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_mail', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Numbers_Orgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_number', models.CharField(max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages_From_Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_content', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages_Orgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_content', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications_Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_message_from_org', models.BooleanField(default=0)),
                ('is_message_from_admin', models.BooleanField(default=0)),
                ('is_request_from_admin', models.BooleanField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('person_in_charge', models.CharField(max_length=100)),
                ('people_working', models.IntegerField(default=0)),
                ('name_of_org', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
