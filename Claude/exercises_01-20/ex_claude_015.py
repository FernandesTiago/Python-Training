def register_book(title, author, year, available):
    book = {"title": title, "author": author, "year": year, "available": available}
    return book

def available_books(book_collection):
    available_list = []
    for book in book_collection:
        if book["available"]:
            available_list.append(book)
    return available_list

def search_by_author(book_collection, author):
    author_books = []
    for book in book_collection:
        if book["author"] == author:
            author_books.append(book)
    return author_books

def oldest_book(book_collection):
    oldest_year = 10000
    oldest = 0
    for book in book_collection:
        if book["year"] < oldest_year:
            oldest_year = book["year"]
            oldest = book
    return oldest

def summary(book_collection):
    available_count = 0
    print()
    for book in book_collection:
        available = book["available"]
        status = "available" if available else "unavailable"
        print(f"Book: {book['title']:<20} Author: {book['author']:20} Year: {book['year']:^6} Availability: {status:<10}")
        if available:
            available_count += 1
    print(f"\n{available_count} books are available")
    oldest = oldest_book(book_collection)
    print(f"\nThe oldest is {oldest['title']}")

collection = [
    register_book("Dom Casmurro", "Machado de Assis", 1899, True),
    register_book("O Cortico", "Aluisio Azevedo", 1890, False),
    register_book("Iracema", "Jose de Alencar", 1865, True),
    register_book("Memorias Postumas", "Machado de Assis", 1881, False),
    register_book("O Guarani", "Jose de Alencar", 1857, True),
]

summary(collection)
