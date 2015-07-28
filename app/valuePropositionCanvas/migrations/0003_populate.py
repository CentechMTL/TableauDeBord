# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def gen_newtype(apps, schema_editor):
        MyModel = apps.get_model('valuePropositionCanvas', 'ValuePropositionCanvasElement')
        MySecondModel = apps.get_model('valuePropositionCanvas', 'ValuePropositionCanvasType')
        for row in MyModel.objects.all():
            id = row.type_id
            for row2 in MySecondModel.objects.all():
                if(row2.id == id):
                    row.newtype = row2.name
                    row.save()

    dependencies = [
        ('valuePropositionCanvas', '0002_valuepropositioncanvaselement_newtype'),
    ]

    operations = [
        migrations.RunPython(gen_newtype, reverse_code=migrations.RunPython.noop),
    ]
