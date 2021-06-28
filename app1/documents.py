from app1.models import Publisher,Book,Author

# from elasticsearch_dsl.connections import connections
# connections.create_connection(hosts=['localhost'], timeout=20)

# class AuthorDocument(Document):
#     class Index:
#         # Name of the Elasticsearch index
#         name = 'author'
#         # See Elasticsearch Indices API reference for available settings
#         settings = {'number_of_shards': 1,
#                     'number_of_replicas': 0}

#     class Django:
#         model = Author # The model associated with this Document

#         # The fields of the model you want to be indexed in Elasticsearch
#         fields = [
#             'first_name',
#             'last_name',
#             'email',
#         ]

from django_elasticsearch_dsl import Document, Index
# from django_elasticsearch_dsl.registries import registry


posts = Index('author')

# @registry.register_document
@posts.document
class AuthorDocument(Document):
    class Django:
        model = Author

        fields = [
            'first_name',
            'last_name',
            'email',
        ]