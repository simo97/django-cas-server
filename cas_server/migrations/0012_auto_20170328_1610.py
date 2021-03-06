# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-28 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cas_server', '0011_auto_20161007_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='federatediendityprovider',
            name='cas_protocol_version',
            field=models.CharField(choices=[('1', 'CAS 1.0'), ('2', 'CAS 2.0'), ('3', 'CAS 3.0'), ('CAS_2_SAML_1_0', 'SAML 1.1')], default='3', help_text='Version of the CAS protocol to use when sending requests the the backend CAS.', max_length=30, verbose_name='CAS protocol version'),
        ),
        migrations.AlterField(
            model_name='servicepattern',
            name='single_log_out_callback',
            field=models.CharField(blank=True, default='', help_text='URL where the SLO request will be POST. empty = service url\nThis is usefull for non HTTP proxied services.', max_length=255, verbose_name='single log out callback'),
        ),
        migrations.AlterField(
            model_name='servicepattern',
            name='user_field',
            field=models.CharField(blank=True, default='', help_text='Name of the attribute to transmit as username, empty = login', max_length=255, verbose_name='user field'),
        ),
    ]
