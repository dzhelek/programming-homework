class Person:
    def __init__(self, name, lastname, age, nationality):
        self.firstname = name
        self.lastname = lastname
        self.age = age
        self.nationality = nationality
    
    def printinfo(self):
        print(f"{self.firstname} {self.lastname} from {self.nationality}")


class Student(Person):
    def __init__(self, name, lname, age, nationality, university, year):
        super().__init__(name, lname, age, nationality)
        self.university = university
        self.year = year
    
    def printinfo(self):
        print(f"{self.firstname} {self.lastname} from {self.nationality}:")
        print(f"{self.university}, {self.year}")


yoan = Student('Yoan', 'Dzhelekarski', 19, 'Bulgaria', 'Technical University of Sofia', 2026)
pavel = Student('Pavel', 'Pavlov', 19, 'Bulgaria', 'Technical university of Sofia', 2026)

yoan.printinfo()
pavel.printinfo()
