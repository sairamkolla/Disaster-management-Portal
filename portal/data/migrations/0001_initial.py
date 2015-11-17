# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressOrgs',
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
            name='ContactMailsOrgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_mail', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactNumbersOrgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact_number', models.CharField(max_length=12)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DecisionsOrgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_accepted', models.IntegerField(default=0)),
                ('seen', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DisasterApprovalAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_visited', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DisasterDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_of_sos_received', models.IntegerField(default=0)),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('disaster_code', models.CharField(max_length=2)),
                ('disaster_name', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=200)),
                ('no_people_affected', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='DisasterProposal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('no_of_sos_received', models.IntegerField(default=0)),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('disaster_code', models.CharField(max_length=2)),
                ('disaster_name', models.CharField(max_length=20)),
                ('reason', models.CharField(default=b'NotKnown', max_length=200)),
                ('no_people_affected', models.IntegerField(default=0)),
                ('is_viewed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='MessagesFromAdmin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_content', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessagesOrgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_content', models.CharField(max_length=256)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orgs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.IntegerField(default=0)),
                ('org_head', models.CharField(max_length=100)),
                ('org_strength', models.IntegerField(default=0)),
                ('name_of_org', models.CharField(max_length=100)),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SosReports',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disaster_code', models.CharField(max_length=2)),
                ('latitude', models.CharField(max_length=15)),
                ('longitude', models.CharField(max_length=15)),
                ('sos_timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_disaster', models.BooleanField(default=0)),
                ('disaster', models.ForeignKey(to='data.DisasterDescription')),
            ],
        ),
        migrations.AddField(
            model_name='messagesorgs',
            name='receiver_org',
            field=models.ForeignKey(related_name='receiver', to='data.Orgs'),
        ),
        migrations.AddField(
            model_name='messagesorgs',
            name='sender_org',
            field=models.ForeignKey(related_name='sender', to='data.Orgs'),
        ),
        migrations.AddField(
            model_name='messagesfromadmin',
            name='target_org',
            field=models.ForeignKey(to='data.Orgs'),
        ),
        migrations.AddField(
            model_name='disasterapprovaladmin',
            name='disaster',
            field=models.ForeignKey(to='data.DisasterDescription'),
        ),
        migrations.AddField(
            model_name='decisionsorgs',
            name='disaster',
            field=models.ForeignKey(to='data.DisasterDescription'),
        ),
        migrations.AddField(
            model_name='decisionsorgs',
            name='org',
            field=models.ForeignKey(to='data.Orgs'),
        ),
        migrations.AddField(
            model_name='contactnumbersorgs',
            name='org',
            field=models.ForeignKey(to='data.Orgs'),
        ),
        migrations.AddField(
            model_name='contactmailsorgs',
            name='org',
            field=models.ForeignKey(to='data.Orgs'),
        ),
        migrations.AddField(
            model_name='addressorgs',
            name='org',
            field=models.ForeignKey(to='data.Orgs'),
        ),
    ]
