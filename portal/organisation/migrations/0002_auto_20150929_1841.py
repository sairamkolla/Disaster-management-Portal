# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0001_initial'),
        ('siteadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications_org',
            name='disaster_id',
            field=models.ForeignKey(blank=True, to='siteadmin.Disaster_Description', null=True),
        ),
        migrations.AddField(
            model_name='notifications_org',
            name='message_from_admin_id',
            field=models.ForeignKey(blank=True, to='organisation.Messages_From_Admin', null=True),
        ),
        migrations.AddField(
            model_name='notifications_org',
            name='message_from_org_id',
            field=models.ForeignKey(blank=True, to='organisation.Messages_Orgs', null=True),
        ),
        migrations.AddField(
            model_name='notifications_org',
            name='target_org_id',
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
