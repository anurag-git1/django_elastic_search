from app1.models import Publisher,Book,Author

from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=['localhost'], timeout=60)


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
        # related_models = [Book]