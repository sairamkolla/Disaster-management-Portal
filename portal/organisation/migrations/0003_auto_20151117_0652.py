# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organisation', '0002_auto_20151103_1057'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address_org',
            name='org_id',
        ),
        migrations.RemoveField(
            model_name='contact_mails_orgs',
            name='org_id',
        ),
        migrations.RemoveField(
            model_name='contact_numbers_orgs',
            name='org_id',
        ),
        migrations.RemoveField(
            model_name='messages_from_admin',
            name='target_org_id',
        ),
        migrations.RemoveField(
            model_name='messages_orgs',
            name='receiver_org_id',
        ),
        migrations.RemoveField(
            model_name='messages_orgs',
            name='sender_org_id',
        ),
        migrations.RemoveField(
            model_name='notifications_org',
            name='disaster_id',
        ),
        migrations.RemoveField(
            model_name='notifications_org',
            name='message_from_admin_id',
        ),
        migrations.RemoveField(
            model_name='notifications_org',
            name='message_from_org_id',
        ),
        migrations.RemoveField(
            model_name='notifications_org',
            name='target_org_id',
        ),
        migrations.DeleteModel(
            name='Address_Org',
        ),
        migrations.DeleteModel(
            name='Contact_Mails_Orgs',
        ),
        migrations.DeleteModel(
            name='Contact_Numbers_Orgs',
        ),
        migrations.DeleteModel(
            name='Messages_From_Admin',
        ),
        migrations.DeleteModel(
            name='Messages_Orgs',
        ),
        migrations.DeleteModel(
            name='Notifications_Org',
        ),
    ]
