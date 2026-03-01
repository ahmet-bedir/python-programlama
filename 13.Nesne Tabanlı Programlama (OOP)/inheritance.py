class Person:
    def __init__(self):
        print("Person Created.")
        
class Student(Person): # Person sınıfından miras alındı.
    def __init__(self):
        print("Student Created.")
        Person.__init__(self) # Person sınıfının __init__ metodunuda alır.  

s1 = Student()