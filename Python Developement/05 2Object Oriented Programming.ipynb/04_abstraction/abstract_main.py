# import the class student
from abstract_method import Student

class School(Student):
    def __init__(self, name, school_name):
        super().__init__(name)
        self.school_name = school_name

    def student_info(Self):
        print(f"The school name :{Self.name} {Self.school_name}")

class Rules(Student):
    def __init__(self, name, rule_name, rounds):
        super().__init__(name)
        self.rule_name = rule_name
        self.rounds = rounds # normal attributes
        

    def student_info(self):
        print(f"The rules of the school : {self.name} :{self.rule_name}")

