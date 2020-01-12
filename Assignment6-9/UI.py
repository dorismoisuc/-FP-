import domain
import services
import repo
import services2
from domain import Rental

class Console(object):

    def ui_add_book(self):
        bid = int(input("The book id is: "))
        titlu = input("The book title is: ")
        autor = input("The book author is: ")
        self.__service.service_add_book(bid,titlu,autor)

    def undo_operation(self) :
        self.__service.undo_Operation()

    def redo_operation(self) :
        self.__service.redo_Operation()

    def ui_print_books(self):
        books = self.__service.service_get_books()
        for book in books:
            print (book)

    def ui_add_client(self):
        cid = int(input("The client id is: "))
        name = input("The client's name is: ")
        self.__service.service_add_client(cid,name)

    def ui_rent_book(self):
        cid = int(input("The client id is: "))
        bid = int(input("The book id is: "))
        rid = int(input("The rental id is: "))
        rentedDate = int(input("The day of the rental is: "))
        self.__serviceRental.rentBook(cid, bid, rid, rentedDate, self.__serviceClient)

    def ui_return_book(self):
        cid = int(input("The client id is: "))
        bid = int(input("The book id is: "))
        returnDate = int(input("The day of the return is: "))
        self.__serviceRental.returnBook(cid,bid,returnDate, self.__serviceClient)

    def ui_print_clients(self):
        clients = self.__service.service_get_clients()
        for client in clients:
            print (client)

    def ui_delete_client(self):
        cid = int(input("The client id to delete is: "))
        self.__service.service_remove_client(cid)

    def ui_delete_book(self):
        bid = int(input("The book id to delete is: "))
        self.__service.service_remove_book(bid)

    def ui_update_book(self):
        bid = int(input("Enter book id: "))
        bookTitle = input("Enter new title: ")
        bookAuthor = input("Enter new author: ")
        self.__service.service_update_book(bid,bookTitle,bookAuthor)

    def ui_update_client(self):
        clientID = int(input("Enter client id: "))
        clientName = input("Enter new client name: ")
        self.__service.service_update_Client(clientID, clientName)

    def ui_print_search_book(self):
        print("You want to search book by: ")
        print("1. ❀ ID")
        print("2. ☛ NAME")
        print("3. ✒ AUTHOR")
        print("4. ✂ TO STOP SEARCHING")

    def ui_searchBook_id(self):
        newList = []
        id = int(input("The id is: "))
        self.__service.service_search_bookbyId(id,newList)
        if newList != []:
            for book in newList:
                print (book)
        else:
            print ("No such book!")

    def ui_searchBook_title(self):
        newList = []
        title = input("The name of the book you are looking for is: ")
        self.__service.service_search_bookbyTitle(title,newList)
        if newList != []:
            for book in newList:
                print (book)
        else:
            print("No such (partial) titles exist!")

    def ui_searchBook_author(self):
        newList =[]
        author = input("The name of the author you are looking for is: ")
        self.__service.service_search_bookbyAuthor(author,newList)
        if newList != []:
            for book in newList:
                print (book)
        else:
            print ("No such (partial) authors exist!")

    #def ui_print_self(self):
        #self.__serviceClient.print_self()

    def ui_print_search_client(self):
        print("You want to search client by: ")
        print("1. ❀ ID")
        print("2. ☛ NAME")
        print("3. ✂ TO STOP SEARCHING")

    def ui_searchClient_id(self):
        newList = []
        id = int(input("The id is: "))
        self.__service.service_search_clientbyId(id, newList)
        if newList != [] :
            for client in newList:
                print (client)
        else :
            print("No such id in the list")

    def ui_searchClient_name(self):
        newList = []
        name = input("The name of the client you are looking for is: ")
        self.__service.service_search_clientbyName(name,newList)
        if newList != []:
            for client in newList:
                print (client)
        else:
            print("No such (partial) names exist!")


    def ui_add_rental(self):
        rentalID = int(input("Enter the rental ID: "))
        bookID = int(input("Enter the book ID: "))
        clientID = int(input("Enter the client ID: "))
        rentDate = int(input("Enter the rental day: "))
        returnDate = int(0)
        self.__service.service_add_rental(rentalID,bookID,clientID,rentDate,returnDate)

    def ui_print_rentals(self):
        rentals = self.__service.service_get_rentals()
        for rental in rentals:
            print (rental)

    def ui_add_return(self):
        rentalID = int(input("Enter the rental ID for the book you want to return: "))
        bid = int(input("The book id is: "))
        cid =int(input("The client id is: "))
        returnDate = int(input("Enter the return day: "))
        self.__service.service_add_return(rentalID, bid, cid, returnDate)

    def ui_most_activeClients(self):
        list = []
        list = self.__service.service_most_active_clients()
        for it in range(0,len(list)):
            print ("| ID: " + str(list[it][0])  + " |" + " | DAYS: " + str(list[it][1]) + " | " + " | NAME: " + str(list[it][2]) + " |")

    def ui_most_rentedBooks(self):
        list = []
        list = self.__service.mostRented()
        for it in range(0,len(list)):
            print ("| BOOK ID: " + str(list[it][0]) +" |" + " | NR OF RENTALS: " + str(list[it][1]) + " |"+" | TITLE: " + str(list[it][2]) + " |"+ " | AUTHOR: " + str(list[it][3]) + " |")


    def ui_most_rentedAut(self):
        list = []
        list = self.__service.mostRentedA()
        for it in range(0,len(list)):
            print ("| AUTHOR: " + str(list[it][0]) +" |" + "| RENTED: " + str(list[it][1]) + " TIME/S " + "|")


    def ui_nr(self):
        self.__service.numberOfrentals()

    def ui_aut(self):
        self.__service.mostRentedA()

    def ui_print_menu(self):
        print ("❋ To add a book type addBook")
        print ("❋ To print the books type printBooks")
        print ("❋ To add a client type addClient")
        print ("❋ To print the clients type printClients")
        print ("❋ To delete a client type deleteClient")
        print ("❋ To delete a book type deleteBook")
        print ("❋ To rent a book type addRental")
        print ("❋ To return a book type addReturn")
        print("❋ To update the client name type updateClient")
        print("❋ To update the book id type updateBook")
        print("❋ To search for a client type searchClient")
        print("❋ To search for a book type searchBook")
        print("❋ To see the most rented books type mostRentedB")
        print("❋ To see the most active clients type mostActiveC")
        print("❋ To see the most rented authors type mostRentedA")
        print("❋ To undo type undo")
        print("❋ To redo type redo")
        print("✂ To exit type exit")


    def __init__(self, service):
        #self.__serviceBook = serviceBook
        #self.__serviceClient = serviceClient
        #self.__serviceRental = serviceRental
        self.__service = service

    def run(self):
        while True:
            command = input("^^^")
            if command == "exit":
                return
            elif command == "addBook":
                self.ui_add_book()
                self.ui_print_menu()
            elif command == "printBooks":
                self.ui_print_books()
                self.ui_print_menu()
            elif command == "addClient":
                self.ui_add_client()
                self.ui_print_menu()
            elif command == "printClients":
                self.ui_print_clients()
                self.ui_print_menu()
            elif command == "deleteClient":
                self.ui_delete_client()
                self.ui_print_menu()
            elif command == "rentBook":
                self.ui_rent_book()
                self.ui_print_menu()
            elif command == "returnBook":
                self.ui_return_book()
                self.ui_print_menu()
            elif command == "deleteBook":
                self.ui_delete_book()
                self.ui_print_menu()
            elif command =="updateBook":
                self.ui_update_book()
                self.ui_print_menu()
            elif command == "updateClient":
                self.ui_update_client()
                self.ui_print_menu()
            elif command == "undo" :
                self.undo_operation()
            elif command == "redo" :
                self.redo_operation()
            elif command == "searchBook":
                self.ui_print_search_book()
                while True:
                    command = input("*s*")
                    if command == "4":
                        return
                    elif command == "1":
                        self.ui_searchBook_id()
                    elif command == "2":
                        self.ui_searchBook_title()
                    elif command == "3":
                        self.ui_searchBook_author()
                    else:
                        print("Invalid command!")
            elif command == "searchClient":
                self.ui_print_search_client()
                while True:
                    command = input("*c*")
                    if command == "3":
                        return
                    elif command == "1":
                        self.ui_searchClient_id()
                    elif command == "2":
                        self.ui_searchClient_name()
                    else:
                        print("Invalid command!")
            elif command == "addRental":
                self.ui_add_rental()
            elif command == "printRentals":
                self.ui_print_rentals()
            elif command == "addReturn":
                self.ui_add_return()
            elif command == "mostRentedBooks":
                self.ui_most_rented_books()
            elif command == "nr":
                self.ui_nr()
            elif command == "mostActiveC":
                self.ui_most_activeClients()
            elif command == "mostRentedB":
                self.ui_most_rentedBooks()
            elif command == "aut":
                self.ui_aut()
            elif command =="mostRentedA":
                self.ui_most_rentedAut()

            else:
                print("invalid command!\n")
