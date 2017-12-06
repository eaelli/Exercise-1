from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,module):
        self.modules.append(module.title)
        self.grades[Module.get_title(module)] = Module.get_grade(module)

    def get_list_modules(self):
        for module in self.modules:
            print(module)

    def get_grades(self):
        for element in self.grades:
            print("%s: %s" %(element, self.grades[element]))


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
