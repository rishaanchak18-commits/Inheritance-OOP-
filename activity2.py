class Person( object ):
    def __init__( self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display1(self):
        print(self.name)
        print(self.idnumber)
class Employee( Person ):
    def __init__( self, name, idnumber, salary, post ):
        self.salary = salary
        self.post = post
        super().__init__(name, idnumber)
    def display2(self):
        print(self.salary)
        print(self.post)
a = Employee('Rahul', 886012, 200000, "Intern")
a.display1()
a.display2()