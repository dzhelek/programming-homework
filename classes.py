class Person:
    def __init__(self, name, lastname, age, nationality):
        self.firstname = name
        self.lastname = lastname
        self.age = age
        self.nationality = nationality
    
    def printinfo(self):
        print(f"{self.firstname} {self.lastname} from {self.nationality}")


yoan = Person('Yoan', 'Dzhelekarski', 19, 'Bulgaria')
pavel = Person('Pavel', 'Pavlov', 19, 'Bulgaria')

yoan.printinfo()
pavel.printinfo()
