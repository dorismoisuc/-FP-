import controller
class UI:

    def __init__(self):
        self.controller = controller.Controller()
        self.controller.generate_students()

    def read_student(self):
        self.controller.read_student()

    def run(self):
        self.controller.print_menu()
        while True:
            cmd = input(">>>")
            if cmd == "exit":
                return
            elif cmd == "+":
                self.read_student()
                self.controller.print_menu()
            elif cmd == "p":
                self.controller.print_students()
                self.controller.print_menu()
            elif cmd == "u":
                self.controller.undo_operation()
                self.controller.print_menu()
            elif cmd == "d":
                self.controller.remove_group()
                self.controller.print_menu()
            else:
                print("Invalid command!")
