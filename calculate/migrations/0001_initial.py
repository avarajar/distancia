# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ciudad'
        db.create_table(u'calculate_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('latitud', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('longitud', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
        ))
        db.send_create_signal(u'calculate', ['Ciudad'])

        # Adding model 'Distance'
        db.create_table(u'calculate_distance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('origen', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('destino', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
            ('distancia', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
        ))
        db.send_create_signal(u'calculate', ['Distance'])


    def backwards(self, orm):
        # Deleting model 'Ciudad'
        db.delete_table(u'calculate_ciudad')

        # Deleting model 'Distance'
        db.delete_table(u'calculate_distance')


    models = {
        u'calculate.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        },
        u'calculate.distance': {
            'Meta': {'object_name': 'Distance'},
            'destino': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'distancia': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origen': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['calculate']