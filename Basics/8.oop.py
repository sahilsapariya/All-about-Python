class Person:
    # class variable
    count = 0

    def __init__(self, name, age):
        # instance variables
        self.name = name
        self.age = age
        Person.count += 1

    def toString(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def is_adult(self):
        return self.age>=18

if __name__ == "__main__":
    person1 = Person("John", 25)
    person2 = Person("Jane", 30)

    print(person1)  # to show the use of __str__ method

    print(person1.age)
    print(person2.toString())
    print(Person.count)
    print(person2.is_adult())

# output:
# Name: John, Age: 25
# 25
# Name: Jane, Age: 30
# 2
# True