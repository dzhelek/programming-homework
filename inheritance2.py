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
        super().printinfo()
        print(f"{self.university}, {self.year}")


class Lector(Person):
    def __init__(self, name, lname, age, nationality, university, xp):
        super().__init__(name, lname, age, nationality)
        self.university = university
        self.experience = xp
    
    def printinfo(self):
        super().printinfo()
        print(f"{self.university}, {self.experience} years of experience")


yoan = Student('Yoan', 'Dzhelekarski', 19, 'Bulgaria', 'Technical University of Sofia', 2026)
pavel = Student('Pavel', 'Pavlov', 19, 'Bulgaria', 'Technical university of Sofia', 2026)

goceva = Lector('Daniela', 'Goceva', 33, 'Bulgaria', 'Technical University of Sofia', 20)
kateto = Lector('Katq', 'Dishlieva', 33, 'Bulgaria', 'Technical University of Sofia', 15)

yoan.printinfo()
pavel.printinfo()

goceva.printinfo()
kateto.printinfo()
