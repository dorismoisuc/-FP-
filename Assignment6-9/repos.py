import domain
import exceptions
import re
from random import randint
import pickle
import IterableDataStructure

class RepoBook:
    def __init__(self):
        self._books = IterableDataStructure.IterableDataStructure()

    def add_book(self,book):
        self._books.append(book)

    def remove_book(self,bookID):
        for book in self.__books:
            if book.get_bid() == bookID:
                self._books.remove(book)
                return

    def generate_books(self):
        books = ["Ion", "Iona", "Povestea lui Harap Alb", "Hanul Ancutei", "Morometii", "O scrisoare pierduta","Enigma Otiliei", "Luceafarul", "Baltagul", "Eu nu strivesc corola de minuni a lumii"]
        authors = ["Ioan Slavici", "Marin Sorescu", "Ion Creanga", "Mihail Sadoveanu", "Marin Preda","Ion Luca Caragiale", "George Calinescu", "Mihai Eminescu", "Mihail Sadoveanu", "Lucian Blaga"]
        bookIds = list(range(10))
        for it in range(1,11):
            index1 = randint(0, len(books) - 1)
            index2 = randint(0, len(authors) - 1)
            bid = bookIds.pop(randint(0, len(bookIds) - 1))
            self.add_book(domain.Book(bid, books[index1], authors[index2]))

    def update_book(self, bookID, book) :
        for it in range(0,len(self._books)):
            if self._books[it].get_bid() == bookID:
                self._books[it] = book
                it = len(self._books) + 1


    def search_book_byID(self,theID,newList):
        for book in self._books:
            if book.get_bid() == theID:
                newList.append(book)

    def search_book_byTitle(self,theTitle,newList):
        allLower = theTitle.lower()
        for book in self._books:
            title = book.get_titlu()
            lower = title.lower()
            allPartial = re.findall(allLower,lower)
            if (allPartial):
                newList.append(book)

    def search_book_byAuthor(self,theAuthor,newList):
        allLower = theAuthor.lower()
        for book in self._books:
            author = book.get_autor()
            lower = author.lower()
            allPartial = re.findall(allLower,lower)
            if (allPartial):
                newList.append(book)

    def search_book_byID_return_author(self,theid):
        for book in self._books:
            if book.get_bid() == theid:
                return book.get_autor()

    def get_all_books(self):
        return self._books[:]

    def set_all_books(self, books):
        self._books = books

class RepoClients:
    def __init__(self):
        self._clients = IterableDataStructure.IterableDataStructure()

    def add_client(self,client):
        self._clients.append(client)

    def remove_client(self,clientID):
        for client in self._clients:
            if client.get_cid() == clientID:
                self._clients.remove(client)
                return

    def get_all_clients(self):
        return self._clients[:]

    def set_all_clients(self, clients) :
        self._clients = clients

    def update_client(self,oldID,client):
        for it in range(0, len(self._clients)) :
            if self._clients[it].get_cid() == oldID :
                self._clients[it] = client
                it = len(self._clients) + 1

    def generate_clients(self):
        names = ["Andrei", "Andreea", "Mihai", "Mihaela", "Andy", "Miruna", "Ramona", "Doris", "Dorian", "Dora"]
        clientIds = list(range(10))
        for it in range(1, 11) :
            index1 = randint(0, len(names) - 1)
            clientId = clientIds.pop(randint(0, len(clientIds) - 1))
            self.add_client(domain.Client(clientId, names[index1]))

    def search_client_byID(self,theID,newList):
        for client in self._clients:
            if client.get_cid() == theID:
                newList.append(client)

    def search_client_byName(self, theName, newList) :
        allLower = theName.lower()
        for client in self._clients :
            name = client.get_nume()
            lower = name.lower()
            allPartial = re.findall(allLower, lower)
            if (allPartial) :
                newList.append(client)

class RepoRental:
        def __init__(self):
            self._rentals = IterableDataStructure.IterableDataStructure()

        def get_rentals(self):
            return self._rentals [:]

        def add_rental(self,rental):
            self._rentals.append(rental)

        def update_for_return(self,rid,returnDate):
            for rental in self._rentals:
                if rental.get_rid() == rid:
                    rental.set_returnDate(returnDate)
                    return

        def set_all_rentals(self, rentals) :
            self._rentals = rentals

class RepoForTests:
    def __init__(self,repoTest):
        self.__repoTest = repoTest

    def add_object_for_test(self,object):
        self.__repoTest.append(object)
        return self.__repoTest[:]

    def remove_object(self,object):
        it = 0
        while it < len(self.__repoTest) :
            if self.__repoTest[it] == object:
                self.__repoTest.remove(self.__repoTest[it])
                it = it - 1
            it = it + 1
        return self.__repoTest

    def update_object(self, oldObject, newObject) :
        for it in range(0, len(self.__repoTest)) :
            if self.__repoTest[it] == oldObject :
                self.__repoTest[it] = newObject
        return self.__repoTest

    def get_all_objects(self) :
        return self.__repoTest[:]


class RepoBookFile(RepoBook):
    def __init__(self,fileName,readBook,writeBook):
        RepoBook.__init__(self)
        self.__fileName = fileName
        self.__readBook = readBook
        self.__writeBook = writeBook

    def readAllFromFile(self):
        self._books = []
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    book = self.__readBook(line)
                    self._books.append(book)

    def writeAllToFile(self):
        with open(self.__fileName, 'w') as f:
            for book in self._books :
                f.write(self.__writeBook(book) + "\n")

    def add_book(self,book):
        self.readAllFromFile()
        RepoBook.add_book(self,book)
        self.writeAllToFile()

    def remove_book(self,bookID):
        self.readAllFromFile()
        RepoBook.remove_book(self,bookID)
        self.writeAllToFile()

    def update_book(self, bookID, book):
        self.readAllFromFile()
        RepoBook.update_book(self,bookID,book)
        self.writeAllToFile()

    def search_book_byAuthor(self,theAuthor,newList):
        self.readAllFromFile()
        RepoBook.search_book_byAuthor(self,theAuthor,newList)

    def search_book_byID(self,theID,newList):
        self.readAllFromFile()
        RepoBook.search_book_byID()

    def search_book_byTitle(self,theTitle,newList):
        self.readAllFromFile()
        RepoBook.search_book_byTitle()

    def search_book_byID_return_author(self,theid):
        self.readAllFromFile()
        return RepoBook.search_book_byID_return_author()

    def get_all_books(self):
        self.readAllFromFile()
        return RepoBook.get_all_books(self)

    def set_all_books(self, books):
        self.readAllFromFile()
        RepoBook.set_all_books()

class RepoClientFile(RepoClients):
    def __init__(self,fileName,readClient,writeClient):
        RepoClients.__init__(self)
        self.__fileName = fileName
        self.__readClient = readClient
        self.__writeClient = writeClient

    def readAllFromFile(self):
        self._clients = []
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines :
                line = line.strip()
                if line != "" :
                    client = self.__readClient(line)
                    self._clients.append(client)

    def writeAllToFile(self):
        with open(self.__fileName, 'w') as f:
            for client in self._clients :
                f.write(self.__writeClient(client) + "\n")

    def add_client(self,client):
        self.readAllFromFile()
        RepoClients.add_client(self,client)
        self.writeAllToFile()

    def remove_client(self,clientID):
        self.readAllFromFile()
        RepoClients.remove_client(self,clientID)
        self.writeAllToFile()

    def update_client(self,oldID,client):
        self.readAllFromFile()
        RepoClients.update_client(self,oldID,client)
        self.writeAllToFile()

    def get_all_clients(self):
        self.readAllFromFile()
        return RepoClients.get_all_clients(self)

    def set_all_clients(self,clients):
        self.readAllFromFile()
        RepoClients.set_all_clients(self,clients)


    def search_client_byID(self,theID,newList):
        self.readAllFromFile()
        RepoClients.search_client_byID(self,theID,newList)

    def search_client_byName(self, theName, newList):
        self.readAllFromFile()
        RepoClients.search_client_byName(self,theName,newList)

class RepoRentalFile(RepoRental):
    def __init__(self,fileName,readRental,writeRental):
        RepoRental.__init__(self)
        self.__fileName = fileName
        self.__readRental = readRental
        self.__writeRental = writeRental

    def readAllFromFile(self):
        self._rentals = []
        with open(self.__fileName, 'r') as f:
            lines = f.readlines()
            for line in lines :
                line = line.strip()
                if line != "" :
                    rental = self.__readRental(line)
                    self._rentals.append(rental)

    def writeAllToFile(self):
        with open(self.__fileName, 'w') as f:
            for rental in self._rentals :
                f.write(self.__writeRental(rental) + "\n")

    def add_rental(self,rental):
        self.readAllFromFile()
        RepoRental.add_rental(self,rental)
        self.writeAllToFile()

    def update_for_return(self,rid,returnDate):
        self.readAllFromFile()
        RepoRental.update_for_return(self,rid,returnDate)
        self.writeAllToFile()

    def get_rentals(self):
        self.readAllFromFile()
        return RepoRental.get_rentals(self)

    def set_all_rentals(self,rentals):
        self.readAllFromFile()
        RepoRental.set_all_rentals(self,rentals)


class RepoBookBinary(RepoBook):

    def __init__(self, fileName, readBook, writeBook):
        RepoBook.__init__(self)
        self.__fileName = fileName
        self.__readBook = readBook
        self.__writeBook = writeBook

    def readAllFromFile(self):
        self._books = []
        with open(self.__fileName, 'rb') as f:
            while True:
                try:
                    line = pickle.load(f)
                    book = self.__readBook(line)
                    self._books.append(book)
                except EOFError:
                    break

    def writeAllToFile(self):
        with open(self.__fileName, 'wb') as f:
            for book in self._books:
                pickle.dump(self.__writeBook(book), f)


    def add_book(self,book):
        self.readAllFromFile()
        RepoBook.add_book(self,book)
        self.writeAllToFile()

    def remove_book(self,bookID):
        self.readAllFromFile()
        RepoBook.remove_book(self,bookID)
        self.writeAllToFile()

    def update_book(self, bookID, book):
        self.readAllFromFile()
        RepoBook.update_book(self,bookID,book)
        self.writeAllToFile()

    def search_book_byAuthor(self,theAuthor,newList):
        self.readAllFromFile()
        RepoBook.search_book_byAuthor(self,theAuthor,newList)

    def search_book_byID(self,theID,newList):
        self.readAllFromFile()
        RepoBook.search_book_byID()

    def search_book_byTitle(self,theTitle,newList):
        self.readAllFromFile()
        RepoBook.search_book_byTitle()

    def search_book_byID_return_author(self,theid):
        self.readAllFromFile()
        return RepoBook.search_book_byID_return_author()

    def get_all_books(self):
        self.readAllFromFile()
        return RepoBook.get_all_books(self)

    def set_all_books(self, books):
        self.readAllFromFile()
        RepoBook.set_all_books(self)


class RepoClientBinary(RepoClients):
    def __init__(self, fileName, readClient, writeClient):
        RepoBook.__init__(self)
        self.__fileName = fileName
        self.__readClient = readClient
        self.__writeClient = writeClient

    def readAllFromFile(self):
        self._clients = []
        with open(self.__fileName, 'rb') as f:
            while True:
                try:
                    line = pickle.load(f)
                    client = self.__readClient(line)
                    self._clients.append(client)
                except EOFError:
                    break

    def writeAllToFile(self) :
        with open(self.__fileName, 'wb') as f :
            for client in self._clients :
                pickle.dump(self.__writeClient(client), f)

    def add_client(self,client):
        self.readAllFromFile()
        RepoClients.add_client(self,client)
        self.writeAllToFile()

    def remove_client(self,clientID):
        self.readAllFromFile()
        RepoClients.remove_client(self,clientID)
        self.writeAllToFile()

    def update_client(self,oldID,client):
        self.readAllFromFile()
        RepoClients.update_client(self,oldID,client)
        self.writeAllToFile()

    def get_all_clients(self):
        self.readAllFromFile()
        return RepoClients.get_all_clients(self)

    def set_all_clients(self,clients):
        self.readAllFromFile()
        RepoClients.set_all_clients(self,clients)


    def search_client_byID(self,theID,newList):
        self.readAllFromFile()
        RepoClients.search_client_byID(self,theID,newList)

    def search_client_byName(self, theName, newList):
        self.readAllFromFile()
        RepoClients.search_client_byName(self,theName,newList)


class RepoRentalsBinary(RepoRental) :
    def __init__(self, fileName, readRental, writeRental) :
        RepoBook.__init__(self)
        self._fileName = fileName
        self.__readRental = readRental
        self.__writeRental = writeRental

    def readAllFromFile(self) :
        self._rentals = []
        with open(self._fileName, 'rb') as f :
            while True :
                try :
                    line = pickle.load(f)
                    rental = self.__readRental(line)
                    self._rentals.append(rental)
                except EOFError :
                    break

    def writeAllToFile(self) :
        with open(self.__fileName, 'wb') as f :
            for rental in self._rentals :
                pickle.dump(self.__writeRental(rental), f)

    def add_rental(self,rental):
        self.readAllFromFile()
        RepoRental.add_rental(self,rental)
        self.writeAllToFile()

    def update_for_return(self,rid,returnDate):
        self.readAllFromFile()
        RepoRental.update_for_return(self,rid,returnDate)
        self.writeAllToFile()

    def get_rentals(self):
        self.readAllFromFile()
        return RepoRental.get_rentals(self)

    def set_all_rentals(self,rentals):
        self.readAllFromFile()
        RepoRental.set_all_rentals(self,rentals)

