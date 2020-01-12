import exceptions


class Validations() :
    def __init__(self) :
        pass

    def validate_book(self, id, book, books) :
        errors = ""
        for book in books :
            if book.get_bid() == id :
                errors += "Book id already exists!"
        if book.get_titlu() == "" :
            errors += "invalid title!"
        if book.get_bid() < 0 :
            errors += "id should be >0 !! "
        if book.get_autor() == "" :
            errors += "invalid author!"
        if len(errors) > 0 :
            raise exceptions.validError(errors)

    def validate_client(self, id, client, clients) :
        errors = ""
        for client in clients :
            if client.get_cid() == id :
                errors += "Client id already exists!"
        if client.get_nume() == "" :
            errors += "invalid name!"
        if client.get_cid() < 0 :
            errors += "id should be >0!! "
        if len(errors) > 0 :
            raise exceptions.validError(errors)

    def validate_rental(self, rid, bid, rental, rentals) :
        errors = ""
        for rental in rentals :
            if rental.get_rid() == rid :
                errors += "Rental id already exists!"
        for rental in rentals :
            if rental.get_bid() == bid and rental.get_returnDate() == int(0):
                errors += "Book id is already in a rental!"
        if rental.get_rentedDate() < 1 and rental.get_rentedDate() > 31:
            errors += "Rent day should be in [1,31]"
        if rental.get_cid() < 0 :
            errors += "invalid client id!"
        if rental.get_bid() < 0 :
            errors += "invalid book id!"
        if rental.get_rid() < 0 :
            errors += "invalid rental id!"
        if len(errors) > 0 :
            raise exceptions.validError(errors)

    def valid_existent_BookID(self, bookID, books) :
        exists = False
        for it in range(0, len(books)) :
            if books[it].get_bid() == bookID :
                exists = True
                it = len(books) + 1
        if exists == False :
            raise exceptions.validError("book id doesn't exist")

    def valid_rental_for_return(self,rid,bid,cid,rentals):
        errors = ""
        #for rental in rentals:
         #   print("return day", rental.get_returnDate())
          #  print("rent day",rental.get_rentedDate())
           # if rental.get_returnDate() < rental.get_rentedDate() :
            #    errors += "The return day can't be < rent day !!"
        for rental in rentals:
            if rental.get_returnDate() < 1 and rental.get_returnDate() > 31:
                errors += "Return day should be in [1,31]"
        if rental.get_bid() != bid:
                errors += "The book id should be the same as the rental's one!"
        if rental.get_cid() != cid:
                errors += "The client id should be the same as the rental's one!"
        if len(errors)>0:
            raise exceptions.validError(errors)

    def valid_existent_clientID(self, clientID, clients) :
        exists = False
        for it in range(0, len(clients)) :
            if clients[it].get_cid() == clientID :
                exists = True
                it = len(clients) + 1
        if exists == False :
            raise exceptions.validError("client id doesn't exist")

    def valid_existent_rentalID(self, rentID, rentals) :
        exists = False
        for it in range(0, len(rentals)) :
            if rentals[it].get_rid() == rentID :
                exists = True
                it = len(rentals) + 1
        if exists == False :
            raise exceptions.validError("rental id doesn't exist")
