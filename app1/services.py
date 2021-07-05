from app1.models import Author,Book

def get_authors(self):
    abc = Book.objects.prefetch_related('authors')
    print("abcabc",abc)
    return list(abc)