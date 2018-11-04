import json
def run():
    with open("button_data.json", "r") as button_file:
        button_dictionary = json_load(button_file)
    with open("student_data.json", "r") as student_file:
        student_dictionary = json_load(student_file)

    #assuming dictionary of key(filter type): value(list of strings)

    DEPARTMENTS = button_dictionary["Departments"]
    CLASSES = button_dictionary["Classes"]
    RESEARCH_TOPICS = button_dictionary["Research Topics"]
