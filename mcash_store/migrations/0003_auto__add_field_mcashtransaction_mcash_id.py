# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MCashTransaction.mcash_id'
        db.add_column(u'mcash_store_mcashtransaction', 'mcash_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MCashTransaction.mcash_id'
        db.delete_column(u'mcash_store_mcashtransaction', 'mcash_id')


    models = {
        u'mcash_store.mcashtransaction': {
            'Meta': {'object_name': 'MCashTransaction'},
            'customer_token': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mcash_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'session_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'mcash_store.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'price': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['mcash_store']