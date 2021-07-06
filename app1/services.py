from app1.models import Author,Book

def get_books():
    abc = Book.objects.prefetch_related('authors')
    # abc = Book.objects.all()
    print("abcabc",abc)
    return list(abc)