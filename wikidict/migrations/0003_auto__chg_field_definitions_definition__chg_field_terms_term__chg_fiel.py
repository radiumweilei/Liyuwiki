# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Definitions.definition'
        db.alter_column(u'wikidict_definitions', 'definition', self.gf('django.db.models.fields.TextField')(max_length=200))

        # Changing field 'Terms.term'
        db.alter_column(u'wikidict_terms', 'term', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30))

        # Changing field 'Terms.modified_time'
        db.alter_column(u'wikidict_terms', 'modified_time', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Definitions.definition'
        db.alter_column(u'wikidict_definitions', 'definition', self.gf('django.db.models.fields.TextField')(max_length=150))

        # Changing field 'Terms.term'
        db.alter_column(u'wikidict_terms', 'term', self.gf('django.db.models.fields.CharField')(max_length=80, unique=True))

        # Changing field 'Terms.modified_time'
        db.alter_column(u'wikidict_terms', 'modified_time', self.gf('django.db.models.fields.DateTimeField')(auto_now=True))

    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'secretballot.vote': {
            'Meta': {'unique_together': "(('token', 'content_type', 'object_id'),)", 'object_name': 'Vote'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vote': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'wikidict.definitions': {
            'Meta': {'object_name': 'Definitions'},
            'Terms': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'term_definitions'", 'to': u"orm['wikidict.Terms']"}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '65', 'blank': 'True'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'definition': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'homepage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'show': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'uid': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'vote_rank': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'vote_rank2': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        u'wikidict.terms': {
            'Meta': {'object_name': 'Terms'},
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_time': ('django.db.models.fields.DateTimeField', [], {}),
            'term': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'term_pinyin': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'uid': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'visit_times': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['wikidict']