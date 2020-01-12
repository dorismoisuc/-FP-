import unittest

class IterableDataStructure:
    def __init__(self):
        self.__index = 0
        self.__list = []

    def __iter__(self):
        return iter(self.__list)

    def __next__(self):
        if self.__index > len(self.__list)+1:
            raise StopIteration
        else:
            self.__index += 1
        return self.__list[self.__index]

    def __len__(self):
        return len(self.__list)

    def __getitem__(self, index):
        return self.__list[index]

    def __setitem__(self, index, value):
        self.__list[index]=value

    #deletes the item at the given index
    def __delitem__(self, index) :
        del self.__list[index]

    #appends an element to the list
    def append(self, element):
        self.__list.append(element)

    def get_list(self):
        return self.__list[:]


def gnome_sort(list,function):
    '''
    Gnome Sort also called Stupid sort is based on the concept
    of a Garden Gnome sorting his flower pots.
    A garden gnome sorts the flower pots by the following method-
    He looks at the flower pot next to him and the previous one;
    if they are in the right order he steps one pot forward,
    otherwise he swaps them and steps one pot backwards.
    If there is no previous pot
    (he is at the starting of the pot line),
    he steps forwards; if there is no pot next to him
    (he is at the end of the pot line), he is done.
    '''
    '''
    the sorting will be done using the function 
    transmitted as a parameter to check whether 2 elements are in order
    '''
    index = 0
    length = len(list)
    if length == 0 or length == 1:
        return
    while index < length:
        if index == 0 :
            index = index + 1
        if function(list[index-1],list[index])==True:
            index += 1
        else:
            list[index],list[index-1] == list[index-1],list[index]
            index = index - 1


#This method filters the elements of a list by a given "acceptance" function
#it is done by creating a new list and returning it
def filter(list,function):
    newList = []
    for index in range(len(list)):
        if function(list[index]) == True:
            newList.append(list[index])
    return newList[:]


