class Book:
    def __init__(self,bid,titlu,autor):
        self._bid = bid
        self._titlu = titlu
        self._autor = autor
        timesRented = 0
        self.__timesRented = timesRented
        aTimesRented = 0
        self.__aTimesRented = aTimesRented
        #self.__rent = rent
        #self.__autorRented = False

    @staticmethod
    def read_book(line) :
        parts = line.split(",")
        return Book(int(parts[0].strip()), parts[1].strip(),parts[2].strip())

    @staticmethod
    def write_book(book):
        return str(book._bid) + "," + book._titlu + "," + book._autor

    def get_bid(self):
        return self._bid

    def get_titlu(self):
        return self._titlu

    def get_autor(self):
        return self._autor

    def get_timesRented(self):
        return self.__timesRented

    def get_aTimesRented(self):
        return self.__aTimesRented

    def set_bid(self,value):
        self._bid = value

    def set_titlu(self,value):
        self._titlu = value

    def set_timesRented(self,value):
        self.__timesRented = value

    def set_autorRented(self,value):
        self._autorRented = value

    def set_aTimesRented(self,value):
        self.__aTimesRented = value

    def __str__(self):
        return str(self._bid) + " " + self._titlu + " scrisa de " + self._autor


class Client:
    def __init__(self,cid,nume):
        self._cid = cid
        self._nume = nume

    def get_cid(self):
        return self._cid

    def get_nume(self):
        return self._nume

    def set_cid(self,value):
        self._cid = value

    def set_nume(self,value):
        self._nume = value

    #def set_hasRented(self,value):
     #   self.__hasRented = True

    def __str__(self):
        return "Client" + " " + str(self._cid) + " " + self._nume

    @staticmethod
    def read_client(line):
        parts = line.split(",")
        return Client(int(parts[0].strip()), parts[1].strip())

    @staticmethod
    def write_client(client):
        return str(client._cid) + "," + client._nume


class Rental:
    def __init__(self,rid,bid,cid,rentedDate,returnDate):
        self.__rid = rid
        self.__bid = bid
        self.__cid = cid
        self.__rentedDate = rentedDate
        self.__returnDate = returnDate
        self.__clientRentals = 0
        #self.__numberOfDays = self.__returnDate-self.__rentedDate
        self.__isRented = False
        self.__isReturned = False

    def get_rid(self):
        return self.__rid

    def set_rid(self, value):
        self.__rid = value

    def get_cid(self):
        return self.__cid

    def set_cid(self,value):
        self.__cid = value

    def get_bid(self):
        return self.__bid

    def get_rented(self):
        return self.__isRented

    def set_rented(self, value):
        self.__isRented = value

    def get_returned(self):
        return self.__isReturned

    def set_returned(self,value1):
        self.__isReturned = value1

    def set_rentedDate(self,value2):
        self.__rentedDate = value2

    def get_rentedDate(self):
        return self.__rentedDate

    def set_returnDate(self,value3):
        self.__returnDate = value3

    def get_returnDate(self):
        return self.__returnDate

    def get_clientRentals(self):
        return self.__clientRentals

    def set_clientRentals(self,value):
        self.__clientRentals = value

    def get_numberOfDays(self):
        return self.__numberOfDays

    def set_numberOfDays(self,value):
        self.__numberOfDays = value

    def __str__(self):
        return "Rental" + " " + str(self.__rid) + " of the book with the id " + str(self.__bid) + " from the client " + str(self.__cid) + " rented on day " + str(self.__rentedDate) + " returned on day " + str(self.__returnDate)

    @staticmethod
    def read_rental(line):
        parts = line.split(",")
        return Rental(int(parts[0].strip()),int(parts[1].strip()),int(parts[2].strip()),int(parts[3].strip()),int(parts[4].strip()))

    @staticmethod
    def write_rental(rental):
        return str(rental.__rid) + "," + str(rental.__bid) + "," + str(rental.__cid) + "," + str(rental.__rentedDate) + "," + str(rental.__returnDate)
