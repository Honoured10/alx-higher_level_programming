#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        :param first_name: A string representing the first name of the student.
        :param last_name: A string representing the last name of the student.
        :param age: An integer representing the age of the student.
        """
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
        
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age should be non-negative number")
        self._age = value
        
    def full_name(self):
        """
        Return the full name of the student
        
        :return: A string containing the full name of the student
        """
        return f"{self._first_name} {self._last_name}"
    
    def to_json(self):
        """
        Returns a dictionary representation of the Student instance.
        
        :return: A dictionary containing the keys 'first_name', 
        'last_name', 'age' and respective values.
        """
        return {'first_name': self._first_name, 'last_name': self._last_name,
                'age': self._age}
