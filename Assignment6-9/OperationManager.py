import repos


class OperationManager:
    def __init__(self, RepoBook, RepoClient, RepoRental) :
        self.__RepoBook = repos.RepoBook()
        self.__RepoBook.set_all_books(RepoBook.get_all_books())
        self.__RepoClient = repos.RepoClients()
        self.__RepoClient.set_all_clients(RepoClient.get_all_clients())
        self.__RepoRental = repos.RepoRental()
        self.__RepoRental.set_all_rentals(RepoRental.get_rentals())
        self.__redoOperationManager = None
        self.__undoOperationManager = None

    def getBook(self):
        return self.__RepoBook

    def getClient(self):
        return self.__RepoClient

    def getRental(self):
        return self.__RepoRental

    def setUndoOpMan(self, opManager):
        self.__undoOperationManager = opManager

    def setRedoOpMan(self, opManager):
        self.__redoOperationManager = opManager

    def getUndoOpMan(self):
        return self.__undoOperationManager

    def getRedoOpMan(self):
        return self.__redoOperationManager
