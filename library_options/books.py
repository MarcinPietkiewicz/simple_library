from typing import List

from models.author import Author
from models.book import Book
from models.first_name import FirstName
from models.last_name import LastName
from models.publisher import Publisher


class Books:
    def add(self):
        print('Dodawanie książki')
        print('-----------------')
        title = input('Tytuł:')
        isbn = input('ISBN(13):')
        description = input('Opis (opcjonalnie):')

        publisher = Publisher().get_or_create(
            name=input('Nazwa wydawnictwa: ')
        )[0]

        # pętla do dodawania autoróœ

        next_author = 't'
        authors = []

        while next_author == 't':
            authors.append(input("Imię i nazwisko autora: "))
            next_author = input('Następny autor? [t/n]')

        authors = self.add_authors(authors)
        book = Book(title=title,isbn=isbn,description=description,publisher=publisher)
        book.save()

        book.authors = authors
        book.update()

        return book.id

    def add_authors(self, authors: List[str]) -> List[Author] or None:
        result = []

        for author_name in authors:
            try:
                first_name, last_name = author_name.split(' ')
            except ValueError:
                    first_name, last_name = author_name, None

            author = Author().get_or_create(
                    first_name=FirstName().get_or_create(name=first_name)[0],
                    last_name=LastName().get_or_create(name=last_name)[0] if last_name else None
                )[0]

            result.append(author)


        return result


        # author = Author().select().join(LastName).where(LastName.name == input())
        #
        # book = Book(book_title=title, book_isbn=isbn)
        #
        # first_name.save()
        # last_name.save()
        #
        # client = LibraryClient(first_name=first_name, last_name=last_name, book_isbn=isbn,
        #                        book_description=description)
        # client.save()
        #
        # return client.id