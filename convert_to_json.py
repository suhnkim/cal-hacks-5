import json
from users import *

def student_to_json(student):
    with open("student_{0}.json".format(student.name), "w") as write_file:
        json.dump(student.to_dictionary(), write_file)

def professor_to_json(professor):
    with open("professor_{0}.json".format(professor.name), "w") as write_file:
        json.dump(professor.to_dictionary(), write_file)

def list_of_profs_to_json(professors):
    professor_dictionary = {}
    index = 1
    for professor in professors:
        professor_dictionary[index] = professor.to_dictionary()
        index +=1
    with open("recommended_professors.json", "w") as write_file:
        json.dump(professor_dictionary, write_file)
