# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'mcash_store_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'mcash_store', ['Product'])

        # Adding model 'MCashTransaction'
        db.create_table(u'mcash_store_mcashtransaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer_token', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'mcash_store', ['MCashTransaction'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'mcash_store_product')

        # Deleting model 'MCashTransaction'
        db.delete_table(u'mcash_store_mcashtransaction')


    models = {
        u'mcash_store.mcashtransaction': {
            'Meta': {'object_name': 'MCashTransaction'},
            'customer_token': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'mcash_store.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'price': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['mcash_store']