# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MCashTransaction.session_id'
        db.delete_column(u'mcash_store_mcashtransaction', 'session_id')

        # Adding field 'MCashTransaction.shopping_cart'
        db.add_column(u'mcash_store_mcashtransaction', 'shopping_cart',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mcash_store.ShoppingCart'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MCashTransaction.session_id'
        db.add_column(u'mcash_store_mcashtransaction', 'session_id',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'MCashTransaction.shopping_cart'
        db.delete_column(u'mcash_store_mcashtransaction', 'shopping_cart_id')


    models = {
        u'mcash_store.mcashtransaction': {
            'Meta': {'object_name': 'MCashTransaction'},
            'customer_token': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mcash_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shopping_cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mcash_store.ShoppingCart']", 'null': 'True'})
        },
        u'mcash_store.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'price': ('django.db.models.fields.FloatField', [], {})
        },
        u'mcash_store.shoppingcart': {
            'Meta': {'object_name': 'ShoppingCart'},
            'amount': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['mcash_store']