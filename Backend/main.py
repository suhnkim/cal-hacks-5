from convert_to_json import *
from users import *
from filters import *
from react_data import *
from professor_data import *

def main():
    #create the Student instance
    student = create_student(student_dictionary)

    #create list of professors
    list_of_professors = generate_list_of_professors()

    #returns the recommended list of professors as a json file
    list_of_profs_to_json(student.recommend(list_of_professors))

if __name__ == '__main__':
    main()
