import domain
import services
import repos
import unittest

import unittest
class PyUnitTests(unittest.TestCase):
    def tests_for_books(self) :
        book1 = domain.Book(123,"Titlu1","Autor1")
        book2 = domain.Book(1234,"Titlu2","Autor2")
        book3 = domain.Book(12345,"Titlu3","Autor3")
        test_book_list = [book1,book2]
        objects = repos.RepoForTests(test_book_list)
        self.assertEqual([book1,book2], objects.get_all_objects())
        self.assertEqual([book1,book3],objects.update_object(book2,book3))
        self.assertEqual([book1,book3,book2], objects.add_object_for_test(book2))
        self.assertEqual([book1,book3],objects.remove_object(book2))

if __name__ == '__main__' :
    unittest.main()

