from models.first_name import FirstName
from models.last_name import LastName
from models.library_client import LibraryClient

class Users:
    """ Zarządzanie użytkownkami biblioteki """
    def add(self) -> int:
        """ Dodawanie nowych użytkowników do bazy """
        first_name = FirstName().get_or_create(name=input('Podaj imię: '))[0] # zwracana tupla, pierwszy element zawiera imie
        last_name = LastName().get_or_create(name=input('Podaj nazwisko: '))[0]

        first_name.save()
        last_name.save()

        client = LibraryClient(first_name=first_name, last_name=last_name)
        client.save()

        return client.id
