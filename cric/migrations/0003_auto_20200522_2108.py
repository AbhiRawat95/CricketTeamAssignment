# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cric', '0002_teamplayers_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cricketteam',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='matchstats',
            name='winner_team',
            field=models.ForeignKey(related_name='winners', blank=True, to='cric.CricketTeam', null=True),
        ),
        migrations.AlterField(
            model_name='teamplayers',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, primary_key=True),
        ),
    ]
