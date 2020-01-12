from typing import Any, Union
import domain
import exceptions
import re
from random import randint

class Repo:
    def __init__(self):
        self.__library = []

    #adds data in library
    def add(self, data):
        if data in self.__library:
            raise exceptions.repoError("existent data!\n")
        self.__library.append(data)


    def searchBook_id(self,key):
        for x in self.__library:
            if x.get_bid() == key:
                print(x)


    def searchBook_id2(self,key):
        for x in self.__library:
            if x.get_bid() == key:
                return x.get_titlu()

    def searchClient_id(self,key):
        for x in self.__library:
            if x.get_cid() == key:
                print ("The client with that id is:", x)


#In this function I get a key to search the name and
#use the lower function to convert all uppercase
#characters in lowercase characters to simplify the
#search.
#Then, use the RegEx(Regural Expression)
#to check if I find any matching strings
#If so, I print it.
    def searchClient_name(self, key):
        b = key.lower()
        for x in self.__library:
            z = x.get_nume()
            t = z.lower()
            y = re.findall(b,t)
            if (y):
                print (x)

    def searchBook_title(self, key):
        b = key.lower()
        for x in self.__library:
            z = x.get_titlu()
            t = z.lower()
            y = re.findall(b,t)
            if (y):
                print (x)

    def searchBook_author(self, key) :
        b = key.lower()
        for x in self.__library :
            z = x.get_autor()
            t = z.lower()
            y = re.findall(b, t)
            if (y) :
                print(x)

    #search by a key
    def search(self, key):
        if key not in self.__library:
            raise exceptions.repoError("non-existent!\n")
        for x in self.__library:
            if x == key:
                return x

    #deletes a client
    def delete(self, key):
        for x in self.__library:
            if x.get_cid() == key:
                self.__library.remove(x)
                return

    #deletes a book
    def delete2(self,key):
        for x in self.__library:
            if x.get_bid() == key:
                self.__library.remove(x)
                return

    #rents a book
    def rentBook(self, bookID, clientID, rentID,data1):
        #value = 0
        for x in self.__library:
            if x.get_bid() == bookID:
                if not x.get_rented():
                    x.set_rid(rentID)
                    x.set_cid(clientID)
                    x.set_rentedDate(data1)
                    x.set_rented(True)
                    x.set_returned(False)
                    print("Book",x.get_bid(),"RENTED")
                    return
                else:
                    print ("BOOK",x.get_bid(),"ALREADY RENTED")

    def generate_books(self):
        books = ["Ion","Iona","Povestea lui Harap Alb", "Hanul Ancutei", "Morometii","O scrisoare pierduta","Enigma Otiliei","Luceafarul","Baltagul","Eu nu strivesc corola de minuni a lumii"]
        authors = ["Ioan Slavici","Marin Sorescu","Ion Creanga","Mihail Sadoveanu","Marin Preda","Ion Luca Caragiale", "George Calinescu","Mihai Eminescu", "Mihail Sadoveanu","Lucian Blaga"]
        bids = list(range(10))
        for it in range(1,11):
           index1 = randint(0,len(books)-1)
           index2 = randint(0,len(authors)-1)
           bid = bids.pop(randint(0,len(bids)-1))
           self.add(domain.Book(bid,books[index1],authors[index2]))


    def generate_clients(self):
        names = ["Andrei","Andreea","Mihai","Mihaela","Andy","Miruna","Radu","Doris","Dorian","Dora"]
        cids = list(range(10))
        for it in range(1,11):
            index = randint(0,len(names)-1)
            cid = cids.pop(randint(0,len(cids)-1))
            self.add(domain.Client(cid,names[index]))

    def generate_rentals(self):
        cids = list(range(10))
        bids = list(range(10))
        rids = list(range(10))
        for it in range(1,11):
            rid = rids.pop(randint(0,len(rids)-1))
            bid = bids.pop(randint(0,len(bids)-1))
            cid = cids.pop(randint(0,len(cids)-1))
            rentDate = 0
            returnDate = 0
            nrofrent = 0
            self.add(domain.Rental(rid,bid,cid,rentDate,returnDate,nrofrent))


    def rentedBooks(self) :
        for x in self.__library :
            if x.get_rented() == True and x.get_returned() == False :
                x.set_returnDate("not yet returned")
                print(x)
            elif x.get_rented() == False and x.get_returned() == True:
                print (x)


    def returnBook(self, bookID,data2) :
        for x in self.__library :
            if x.get_bid() == bookID :
                if not x.get_returned() :
                    x.set_returnDate(data2)
                    x.set_returned(True)
                    x.set_rented(False)
                    if x.get_nrofrent() != 0:
                        x.set_nrofrent(x.get_nrofrent()+1)
                    else:
                        x.set_nrofrent(1)
                    print("Book",x.get_bid(),"RETURNED")
                    return
                else :
                    print("Book",x.get_bid(),"ALREADY RETURNED")

    def most_rentedBooks(self):
        listofrented = []
        for x in self.__library:
            y = x.get_nrofrent()
            listofrented.append([y,x.get_bid()])
        listofrented.sort(reverse=True)
        for it in range(0, len(listofrented) - 1) :
            print("Rented", listofrented[it][0], "times with the BOOK ID", listofrented[it][1])


    #updates the id of a book
    def update(self, i_d, newid):
        for x in self.__library:
            if x.get_bid() == i_d:
                x.set_bid(newid)
                return

    #updates the id of a client
    def update2(self,oldName,newName):
        for x in self.__library:
            if x.get_nume() == oldName:
                x.set_nume(newName)
                return

    #gets all data from library
    def get_data(self):
        return self.__library[:]

    #returns the length of the library
    def length(self):
        return len(self.__library)

    def service_most_rented_book(self):
        rentals = RepoRental.get_rentals(self.__RepoRental)
        most_rented_books = {}
        for rental in rentals:
            most_rented_books[rental.get_nrofrent()] = 0
        for rental in rentals:
            number = rental.get_nrofrent()
            most_rented_books[rental.get_nrofrent()] += number
        sort_books = sorted(most_rented_books.items(),key = lambda x:x[1],reverse=True)
        for it in range(0,len(sort_books)):
            sort_books[it] = list(sort_books[it])
        books = RepoBook.get_all_books(self.__RepoBook)
        for it in range(0,len(sort_books)):
            for j in range(0,len(books)):
                if sort_books[it][0] == books[j].get_bid():
                    sort_books[it].append(books[j].get_titlu())
                    j = len(books) + 1
        return sort_books