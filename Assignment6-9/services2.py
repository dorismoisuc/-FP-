from repos import RepoBook, RepoClients, RepoRental
import domain
import exceptions
import validations
from random import randint
from datetime import date
import OperationManager
from IterableDataStructure import IterableDataStructure, gnome_sort

class Service :
    def __init__(self, RepoBook, RepoClient, RepoRental, validations) :
        self.__RepoBook = RepoBook
        self.__RepoClient = RepoClient
        self.__RepoRental = RepoRental
        self.__validations = validations
        self.__operationManager = OperationManager.OperationManager(RepoBook, RepoClient, RepoRental)

    def service_add_book(self, bookID, title, author) :
        x = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        x.setUndoOpMan(self.__operationManager.getUndoOpMan())
        book = domain.Book(bookID, title, author)
        books = RepoBook.get_all_books(self.__RepoBook)
        try :
            self.__validations.Validations.validate_book(self.__validations, bookID, book, books)
            self.__RepoBook.add_book(book)
        except Exception as ex :
            print(str(ex))
        y = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        y.setUndoOpMan(x)
        x.setRedoOpMan(self.__operationManager)
        self.__operationManager = y

    def undo_Operation(self) :
        x = self.__operationManager.getUndoOpMan()
        if x is None :
            print("no more undos")
        else:
            self.__RepoBook = x.getBook()
            self.__RepoClient = x.getClient()
            self.__RepoRental = x.getRental()
            x.setRedoOpMan(self.__operationManager)
            x.setUndoOpMan(x.getUndoOpMan())
            self.__operationManager = x

    def redo_Operation(self) :
        x = self.__operationManager.getRedoOpMan()
        if x is None :
            print("no more redos")
        else:
            self.__RepoBook = x.getBook()
            self.__RepoClient = x.getClient()
            self.__RepoRental = x.getRental()

            x.setUndoOpMan(self.__operationManager)
            x.setRedoOpMan(x.getRedoOpMan())
            self.__operationManager = x

    def service_add_client(self, clientID, name) :
        x = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        x.setUndoOpMan(self.__operationManager.getUndoOpMan())
        client = domain.Client(clientID, name)
        clients = RepoClients.get_all_clients(self.__RepoClient)
        try :
            self.__validations.Validations.validate_client(self.__validations, clientID, client, clients)
            self.__RepoClient.add_client(client)
        except Exception as ex :
            print(str(ex))
        y = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        y.setUndoOpMan(x)
        x.setRedoOpMan(self.__operationManager)
        self.__operationManager = y

    def service_get_books(self) :
        return RepoBook.get_all_books(self.__RepoBook)

    #def compare(self,element1,element2):
     #   if element1.() > element2.() :
      # elif element1.() < element2.() :
       #     return False
        #else :
         #   return element1.() >= element2.()


    def service_get_clients(self) :
        return RepoClients.get_all_clients(self.__RepoClient)

    def service_remove_book(self, bookID) :
        x = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        x.setUndoOpMan(self.__operationManager.getUndoOpMan())
        books = RepoBook.get_all_books(self.__RepoBook)
        try :
            self.__validations.Validations.valid_existent_BookID(self.__validations, bookID, books)
            self.__RepoBook.remove_book(bookID)
        except Exception as ex :
            print(str(ex))
        y = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        y.setUndoOpMan(x)
        x.setRedoOpMan(self.__operationManager)
        self.__operationManager = y

    def service_remove_client(self, clientID) :
        x = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        x.setUndoOpMan(self.__operationManager.getUndoOpMan())
        clients = RepoClients.get_all_clients(self.__RepoClient)
        try :
            self.__validations.Validations.valid_existent_clientID(self.__validations, clientID, clients)
            self.__RepoClient.remove_client(clientID)
        except Exception as ex :
            print(str(ex))
        y = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        y.setUndoOpMan(x)
        x.setRedoOpMan(self.__operationManager)
        self.__operationManager = y

    def service_update_book(self, bookID, title, author) :
        x = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        x.setUndoOpMan(self.__operationManager.getUndoOpMan())
        book = domain.Book(bookID,title,author)
        books = RepoBook.get_all_books(self.__RepoBook)
        try :
            self.__validations.Validations.valid_existent_BookID(self.__validations, bookID, books)
            self.__RepoBook.update_book(bookID, book)
        except Exception as ex :
            print(str(ex))
        y = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        y.setUndoOpMan(x)
        x.setRedoOpMan(self.__operationManager)
        self.__operationManager = y

    def service_update_Client(self, clientID, clientName) :
        x = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        x.setUndoOpMan(self.__operationManager.getUndoOpMan())
        client = domain.Client(clientID,clientName)
        clients = RepoClients.get_all_clients(self.__RepoClient)
        try :
            self.__validations.Validations.valid_existent_clientID(self.__validations,clientID,clients)
            self.__RepoClient.update_client(clientID,client)
        except Exception as ex :
            print(str(ex))
        y = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        y.setUndoOpMan(x)
        x.setRedoOpMan(self.__operationManager)
        self.__operationManager = y

    def service_search_clientbyId(self, clientID, newList) :
        clients = RepoClients.get_all_clients(self.__RepoClient)
        try :
            self.__validations.Validations.valid_existent_clientID(self.__validations, clientID, clients)
            self.__RepoClient.search_client_byID(clientID, newList)
        except Exception as ex :
            print(str(ex))

    def service_search_clientbyName(self, clientName, newList) :
        clients = RepoClients.get_all_clients(self.__RepoClient)
        try :
            self.__RepoClient.search_client_byName(clientName, newList)
        except Exception as ex :
            print(str(ex))

    def service_search_bookbyId(self, bookID, newList) :
        books = RepoBook.get_all_books(self.__RepoBook)
        try :
            self.__validations.Validations.valid_existent_BookID(self.__validations, bookID, books)
            self.__RepoBook.search_book_byID(bookID, newList)
        except Exception as ex :
            print(str(ex))

    def service_search_bookbyTitle(self, bookTitle, newList) :
        books = RepoBook.get_all_books(self.__RepoBook)
        try :
            self.__RepoBook.search_book_byTitle(bookTitle, newList)
        except Exception as ex :
            print(str(ex))

    def service_search_bookbyAuthor(self, bookAuthor, newList) :
        books = RepoBook.get_all_books(self.__RepoBook)
        try :
            self.__RepoBook.search_book_byAuthor(bookAuthor, newList)
        except Exception as ex :
            print(str(ex))

    def addTimesRented(self,bookID):
        books = RepoBook.get_all_books(self.__RepoBook)
        for book in books:
            if book.get_bid() == bookID:
                book.set_timesRented(book.get_timesRented()+1)

    def addTimesRentedAut(self,bookID):
        books = RepoBook.get_all_books(self.__RepoBook)
        author = RepoBook.search_book_byID_return_author(self.__RepoBook,bookID)
        for book in books:
            if book.get_bid() == bookID:
                if book.get_autor() == author:
                    book.set_aTimesRented(book.get_aTimesRented()+1)

    def service_add_rental(self, rentalID, bookID, clientID, rentedDate, returnDate) :
        x = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        x.setUndoOpMan(self.__operationManager.getUndoOpMan())
        rental = domain.Rental(rentalID, bookID, clientID, rentedDate, returnDate)
        rentals = RepoRental.get_rentals(self.__RepoRental)
        books = RepoBook.get_all_books(self.__RepoBook)
        try :
            self.__validations.Validations.validate_rental(self.__validations, rentalID, bookID, rental, rentals)
            self.__RepoRental.add_rental(rental)
            self.addTimesRented(bookID)
            self.addTimesRentedAut(bookID)
        except Exception as ex :
            print(str(ex))
        y = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        y.setUndoOpMan(x)
        x.setRedoOpMan(self.__operationManager)
        self.__operationManager = y

    def service_get_rentals(self) :
        return RepoRental.get_rentals(self.__RepoRental)

    def service_add_return(self, rid, bid, cid, returnDate) :
        x = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        x.setUndoOpMan(self.__operationManager.getUndoOpMan())
        rentals = RepoRental.get_rentals(self.__RepoRental)
        try :
            self.__validations.Validations.valid_existent_rentalID(self.__validations, rid, rentals)
            self.__validations.Validations.valid_rental_for_return(self.__validations, rid, bid, cid,rentals)
            self.__RepoRental.update_for_return(rid, returnDate)
        except Exception as ex :
            print(str(ex))
        y = OperationManager.OperationManager(self.__RepoBook, self.__RepoClient, self.__RepoRental)
        y.setUndoOpMan(x)
        x.setRedoOpMan(self.__operationManager)
        self.__operationManager = y

    def service_most_active_clients(self) :
        rentals = RepoRental.get_rentals(self.__RepoRental)
        today = date.today()
        most_active_clients = {}
        for rental in rentals :
            most_active_clients[rental.get_cid()] = 0
        for rental in rentals :
            data1 = rental.get_rentedDate()
            if rental.get_returnDate() != int(0) :
                data2 = rental.get_returnDate()
            else :
                data2 = int(today.day)
            days = abs(data1 - data2)
            most_active_clients[rental.get_cid()] += days
        sort_clients = sorted(most_active_clients.items(), key=lambda x : x[1], reverse=True)
        for it in range(0, len(sort_clients)) :
            sort_clients[it] = list(sort_clients[it])
        clients = RepoClients.get_all_clients(self.__RepoClient)
        for it in range(0, len(sort_clients)) :
            for j in range(0, len(clients)) :
                if sort_clients[it][0] == clients[j].get_cid() :
                    sort_clients[it].append(clients[j].get_nume())
                    j = len(clients) + 1
        return sort_clients

    def mostRented(self) :
        books = RepoBook.get_all_books(self.__RepoBook)
        most_rented_books = {}
        for book in books:
            most_rented_books[book.get_bid()]=0
        for book in books:
            nr = book.get_timesRented()
            most_rented_books[book.get_bid()] += nr
        sort_books = sorted(most_rented_books.items(), key = lambda x : x[1],reverse=True)
        for it in range(0,len(sort_books)):
            sort_books[it] = list(sort_books[it])
        for it in range(0,len(sort_books)):
            for j in range(0,len(books)):
                if sort_books[it][0] == books[j].get_bid():
                    sort_books[it].append(books[j].get_titlu())
                    sort_books[it].append(books[j].get_autor())
                    j = len(books) + 1
        return sort_books

    def mostRentedA(self):
        books = RepoBook.get_all_books(self.__RepoBook)
        most_rented_authors = {}
        for book in books:
           most_rented_authors[book.get_autor()] = 0
        for book in books:
            nr = book.get_aTimesRented()
            most_rented_authors[book.get_autor()] += nr
        sort_authors = sorted(most_rented_authors.items(), key = lambda x:x[1],reverse=True)
        for it in range(0,len(sort_authors)):
            sort_authors[it] = list(sort_authors[it])
        for it in range(0,len(sort_authors)):
            for j in range(0,len(books)):
                if sort_authors[it][0] == books[j].get_autor():
                    sort_authors[it].append(books[j].get_autor())
                    j = len(books) +1
        return sort_authors


