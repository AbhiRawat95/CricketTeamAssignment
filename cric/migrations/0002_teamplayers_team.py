# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cric', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamplayers',
            name='team',
            field=models.ForeignKey(related_name='players_team', on_delete=django.db.models.deletion.PROTECT, verbose_name='Team', blank=True, to='cric.CricketTeam', null=True),
        ),
    ]
