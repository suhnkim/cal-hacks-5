import json
from users import *

def generate_list_of_professors():
    with open("professors.json", "r") as professor_file:
        professor_dictionary = json_load(professor_file)
        list_of_professors = []
        for professor in professor_dictionary:
            name = professor_dictionary["Name"]
            department = professor_dictionary["Department"]
            classes_teaching = professor_dictionary["Classes"]
            research_topics = professor_dictionary["Research Topics"]
            interest = professor_dictionary["Interests"]
            bio = professor_dictionary["Bio"]
            email = professor_dictionary["Email"]
            website = professor_dictionary["Website"]
            calendar = professor_dictionary["Calendar"]
            list_of_professors.append(Professor(calendar, name, department, classes_teaching
                                    research_topics, interest, bio, email, website))
        return list_of_professors
