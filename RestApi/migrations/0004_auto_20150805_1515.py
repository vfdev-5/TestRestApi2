# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('RestApi', '0003_auto_20150805_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(related_name='image', to=settings.AUTH_USER_MODEL),
        ),
    ]
