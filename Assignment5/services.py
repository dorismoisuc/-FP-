import student

# validates the data from the input
def validate_data(stud_id, name, group):
    ok = True
    if not stud_id.isdigit() or int(stud_id) <= 0:
        ok = False
    if not isinstance(name, str):
        ok = False
    if not group.isdigit() or int(group) <= 0:
        ok = False
    return ok


class Service:
    def __init__(self):
        self.listOfStudents = []
        self.listOfListOfStudents = []

    # generates a premade list of students
    def generate_students(self):
        self.listOfStudents.append(student.Student(1, "Gabi", 1))
        self.listOfStudents.append(student.Student(2, "Andy", 1))
        self.listOfStudents.append(student.Student(3, "Marian", 1))
        self.listOfStudents.append(student.Student(4, "Raluca", 2))
        self.listOfStudents.append(student.Student(5, "Andrei", 2))
        self.listOfStudents.append(student.Student(6, "Calin", 2))
        self.listOfStudents.append(student.Student(7, "Alina", 3))
        self.listOfStudents.append(student.Student(8, "Andreea", 3))
        self.listOfStudents.append(student.Student(9, "Maia", 3))
        self.listOfStudents.append(student.Student(10, "Cristian", 4))

    # reads student from the console then adds them to the list of students
    def read_student(self):
        stud_id = input("insert id: ")
        name = input("insert name: ")
        group = input("insert group: ")

        # checks if a student id is already in the list, if it is it returns a proper message
        for it in self.listOfStudents:
            if int(it.getId()) == int(stud_id):
                print("Duplicate id.")
                return False

        result = validate_data(stud_id, name, group)

        # if all the data from input is validated then the student is added
        if result:
            self.listOfListOfStudents.append(self.listOfStudents[:])
            self.listOfStudents.append(student.Student(stud_id, name, group))

        else:
            print("Input not valid.")
            return False

    # the undo operation
    # if the list of lists ( where all the lists are put after an operation) is null, then you can't do more undos
    # else from the lists of lists you get the last version of the list
    def undo_operation(self):
        if len(self.listOfListOfStudents) > 0:
            self.listOfStudents = self.listOfListOfStudents.pop()
        else:
            print("No Undo")

    # prints the students (id,name,group)
    def print_students(self):
        for it in self.listOfStudents:
            print(str(it.getId()) + " " + it.getName() + " " + str(it.getGroup()))

    # removes a given group and their students

    def remove_group(self):
        group = input("insert group you want to delete: ")
        el_removed = False
        temp = self.listOfStudents[:]
        self.listOfListOfStudents.append(self.listOfStudents[:])
        for it in temp:
            if int(it.getGroup()) == int(group):
                self.listOfStudents.remove(it)
                el_removed = True

        if not el_removed:
            self.listOfListOfStudents.pop()

    # the menu
    def print_menu(self):
        print("If you want to add a student type +")
        print("If you want to print the list of students type p")
        print("If you want to delete a group type d")
        print("If you want to undo type u")
        print("If you want to exit type exit")


"""

def test_add():

    student1=student.Student(11,"ghita",3)
    Controller.read_student(student1)
    student2=student.Student(11,"gheorghe",4)
    Controller.read_student(student2)
    try:
        read_student(student2)
        assert(False)
    except Exception as ex:
        assert(str(ex)=="existing id!")
"""