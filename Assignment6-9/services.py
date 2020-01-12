import domain
import repo
#import valid


class serviceBook():
    def __init__(self, repoBook):
        self.__repoBook = repoBook


    def add_book(self, bid, titlu, autor):
        book = domain.Book(bid, titlu, autor)
        self.__repoBook.add(book)

    def get_books(self):
        return self.__repoBook.get_data()

    def delete_book(self,bid):
        self.__repoBook.delete2(bid)

    def update_book(self,bid,newid):
        self.__repoBook.update(bid,newid)

    def search_book_ID(self,bid):
        self.__repoBook.searchBook_id(bid)

    def search_book_title(self,key):
        self.__repoBook.searchBook_title(key)

    def search_book_author(self,key):
        self.__repoBook.searchBook_author(key)

class serviceClient():
    def __init__(self, repoClient):
        self.__repoClient = repoClient

    def add_client(self, cid, nume):
        client = domain.Client(cid, nume)
        self.__repoClient.add(client)

    def get_clients(self):
        return self.__repoClient.get_data()

    def delete_client(self, cid):
        self.__repoClient.delete(cid)

    def update_client(self,oldName,newName):
        self.__repoClient.update2(oldName,newName)

    def search_client_ID(self,cid):
        self.__repoClient.searchClient_id(cid)

    def search_client_name(self,nume):
        self.__repoClient.searchClient_name(nume)

class serviceRental():
    def __init__(self,repoRental):
        self.__repoRental = repoRental

    def rented_books(self):
        self.__repoRental.rentedBooks()

    def nr_of_rent(self):
        self.__repoRental.nrOfRentals()

    def rentBook(self, cid, bid, rid, rentedDate, clientRepo):
            # verifica daca exista client si carte
            self.__repoRental.rentBook(bid,cid,rid,rentedDate)

    def returnBook(self, cid, bid, returnDate, clientRepo) :
            self.__repoRental.returnBook(bid,returnDate)

    def mostRented(self):
        self.__repoRental.most_rentedBooks()