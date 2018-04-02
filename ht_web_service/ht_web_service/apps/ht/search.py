from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from ht_web_service.apps.ht import models

connections.create_connection()


class FeatureIndex(DocType):
    order = Text()
    event = Text()
    piquetu = Text()

    class Meta:
        index = 'feature-index'


def bulk_indexing():
    FeatureIndex.init()
    es = Elasticsearch()
    bulk(client=es, actions=(b.indexing() for b in models.Feature.objects.all().iterator()))
