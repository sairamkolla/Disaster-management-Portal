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
            ],
        ),
        migrations.CreateModel(
            name='Contact_Mails_Orgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_mail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Numbers_Orgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_number', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Messages_From_Admin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Messages_Orgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_content', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Name_Orgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Notifications_Org',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_message_from_org', models.BooleanField(default=0)),
                ('is_message_from_admin', models.BooleanField(default=0)),
                ('is_request_from_admin', models.BooleanField(default=0)),
                ('disaster_id', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('message_from_admin_id', models.ForeignKey(to='organisation.Messages_From_Admin')),
                ('message_from_org_id', models.ForeignKey(to='organisation.Messages_Orgs')),
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
            ],
        ),
        migrations.AddField(
            model_name='notifications_org',
            name='target_org_id',
            field=models.ForeignKey(to='organisation.Orgs'),
        ),
        migrations.AddField(
            model_name='name_orgs',
            name='org_id',
            field=models.ForeignKey(to='organisation.Orgs'),
        ),
        migrations.AddField(
            model_name='messages_orgs',
            name='receiver_org_id',
            field=models.ForeignKey(related_name='receiver', to='organisation.Orgs'),
        ),
        migrations.AddField(
            model_name='messages_orgs',
            name='sender_org_id',
            field=models.ForeignKey(related_name='sender', to='organisation.Orgs'),
        ),
        migrations.AddField(
            model_name='messages_from_admin',
            name='target_org_id',
            field=models.ForeignKey(to='organisation.Orgs'),
        ),
        migrations.AddField(
            model_name='contact_numbers_orgs',
            name='org_id',
            field=models.ForeignKey(to='organisation.Orgs'),
        ),
        migrations.AddField(
            model_name='contact_mails_orgs',
            name='org_id',
            field=models.ForeignKey(to='organisation.Orgs'),
        ),
        migrations.AddField(
            model_name='address_org',
            name='org_id',
            field=models.ForeignKey(to='organisation.Orgs'),
        ),
    ]
