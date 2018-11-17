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

def create_student(student_data, button_data):
    for key in input_data:
        if key == "Calendar":
            calendar = input_data[key]
        elif key == "Name":
            name = input_data[key]
        elif key == "Departments":
            departments = input_data[key]
        elif key == "Classes":
            classes = input_data[key]
        elif key == "Interests":
            interests = input_data[key]
        elif key == "Filters":
            filter_types = input_data[key]
    filters = []
    for type in filter_types:
        filters.append(Filter(type))
    return Student(calendar, name, departments, classes, interests, filters)
