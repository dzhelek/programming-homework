class Person:
    def __init__(self, name, lastname, age, nationality):
        self.firstname = name
        self.lastname = lastname
        self.age = age
        self.nationality = nationality
    
    def printinfo(self):
        print(f"{self.firstname} {self.lastname} from {self.nationality}")


class Lector(Person):
    def __init__(self, name, lname, age, nationality, university, xp):
        super().__init__(name, lname, age, nationality)
        self.university = university
        self.experience = xp
    
    def printinfo(self):
        super().printinfo()
        print(f"{self.university}, {self.experience} years of experience")


def most_experienced(lectors):
    result = lectors[0]
    for lector in lectors:
        if lector.experience > result.experience:
            result = lector
    return result


goceva = Lector('Daniela', 'Goceva', 33, 'Bulgaria', 'Technical University of Sofia', 20)
kateto = Lector('Katq', 'Dishlieva', 33, 'Bulgaria', 'Technical University of Sofia', 15)
tudjarov = Lector('Boris', 'Tudjarov', 33, 'Bulgarian', 'Technical University of Sofia', 22)
koprinkov = Lector('Ivan', 'Koprinkov', 33, 'Bulgarian', 'Technical University of Sofia', 31)
zadnik = Lector('Zadnik', 'Zadnikov', 78, 'Turkey', 'Sofia University', 55)

most_experienced([goceva, kateto, tudjarov, koprinkov, zadnik]).printinfo()