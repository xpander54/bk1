# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Feed'
        db.create_table(u'newsfeed_feed', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('descripcion', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'newsfeed', ['Feed'])

        # Adding model 'Suscriptor'
        db.create_table(u'newsfeed_suscriptor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feed', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['newsfeed.Feed'])),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=100)),
            ('activo', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('creado', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'newsfeed', ['Suscriptor'])


    def backwards(self, orm):
        # Deleting model 'Feed'
        db.delete_table(u'newsfeed_feed')

        # Deleting model 'Suscriptor'
        db.delete_table(u'newsfeed_suscriptor')


    models = {
        u'newsfeed.feed': {
            'Meta': {'object_name': 'Feed'},
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descripcion': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'newsfeed.suscriptor': {
            'Meta': {'object_name': 'Suscriptor'},
            'activo': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'creado': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '100'}),
            'feed': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['newsfeed.Feed']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['newsfeed']