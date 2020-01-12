import controller


class Student:

    def __init__(self, stud_id, name, group):

        self.stud_id = stud_id

        self.name = name

        self.group = group

    def getId(self):
        return self.stud_id

    def getName(self):
        return self.name

    def getGroup(self):
        return self.group

    def setId(self,value):
        if value <= 0:
            raise ValueError("Id cannot be <= 0!")
        self.stud_id = value

    def setName(self,value):
        if type(value) != str:
            raise ValueError("Name must be a string!")
        self.name = value

    def setGroup(self, value):
        if value <= 0:
            raise ValueError("Group cannot be <= 0!")
        self.group = value



def test_create_student():
    student1 = Student(99,"Andy",92) #creates the student 1 with id=99, name=Andy, group = 92
    assert student1.getId() == 99
    assert student1.getName() == "Andy"
    assert student1.getGroup() == 92
    student2 = Student(98,"Diana",92) # creates the student 2 with id =98, name = Diana, group = 92
    assert student2.getId() == 98
    assert student2.getName() == "Diana"
    assert student2.getGroup() == 92


test_create_student()