"""
high level support for doing this and that.
"""
from django_elasticsearch_dsl import Document, Index
# from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.connections import connections
from app1.models import Book,Author
connections.create_connection(hosts=['localhost','https://django-elastic.herokuapp.com/'], timeout=60)

posts = Index('author')
post = Index('book')

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
@post.document
class BookDocument(Document):
    class Django:
        model = Book

        fields = [
            'title',
        ]
