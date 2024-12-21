from abc import ABC, abstractmethod

class Student(ABC): #importation
    def __init__(self, name):
        self.name = name

    @abstractmethod # shows the functionality
    def student_info(self):
       pass # hiding the how to going to start

    def display(self):
        print("this not the abstract method")

    def display1(self, show):
        self.show = show