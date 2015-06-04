# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    def gen_newtype(apps, schema_editor):
        MyModel = apps.get_model('businessCanvas', 'BusinessCanvasElement')
        MySecondModel = apps.get_model('businessCanvas', 'BusinessCanvasType')
        for row in MyModel.objects.all():
            id = row.type_id
            for row2 in MySecondModel.objects.all():
                if(row2.id == id):
                    row.newtype = row2.name
                    row.save()

    dependencies = [
        ('businessCanvas', '0002_businesscanvaselement_newtype'),
    ]

    operations = [
        migrations.RunPython(gen_newtype, reverse_code=migrations.RunPython.noop),
    ]
