# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-28 15:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    replaces = [(b'backend_citizen', '0001_initial'), (b'backend_citizen', '0002_auto_20160426_1405'), (b'backend_citizen', '0003_auto_20160426_1432')]

    dependencies = [
        ('popolo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
    ]