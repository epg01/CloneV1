"""
In this file we will work on the creation of classes
for the creation of a CRUD
"""
import uuid

class Person:

    def __init__(self, name=None, age=None, date=None):
        """
        instance attribute initialization,
        each attribute is a characteristic
        that defines a person in small traits.
        """
        
        self.__name = name
        self.__age = age
        self.__date = date
        self.id = str(uuid.uuid4())

    @property
    def name(self):
        """
        In this part of the code, the instance attribute is obtained
        name and then in the setter part, assign a value to it.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        In this part of the code we assign the values ​​to the class attribute
        name obtained in the previous step property and we verify that there is no error.
        """
        if not isinstance(name, str):
            raise TypeError("Please enter a correct value")
        elif name is None:
            self.__name = None
        else:
            self.__name = name

    @property
    def age(self):
        """
        In this part of the code, the instance attribute is obtained
        age and then in the setter part, assign a value to it.
        """
        return self.__age

    @age.setter
    def age(self, age):
        """
        In this part of the code we assign the values ​​to the class attribute
        age obtained in the previous step property and we verify that there is no error.
        """
        if not isinstance(age, int):
            raise TypeError("Please enter a correct value")
        elif age is None:
            self.__age = None
        else:
            self.__age = age

    @property
    def date(self):
        """
        In this part of the code, the instance attribute is obtained
        date and then in the setter part, assign a value to it.
        """
        return self.__date

    @date.setter
    def date(self, date):
        """
        In this part of the code we assign the values ​​to the class attribute
        date obtained in the previous step property and we verify that there is no error.
        """
        if not isinstance(date, str):
            raise TypeError("Please enter a correct value")
        elif date is None:
            self.__date = None
        else:
            self.__date = date
    



if __name__ == "__main__":
    juan = Person()
    print(juan.created_at)