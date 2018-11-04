from react_data import *

class Filter():

    def __init__(self, type):
        if type =="time":
            self.perform_filter = time_filter
        elif type == "department":
            self.deparments = DEPARTMENTS
            self.perform_filter = department_filter
        elif type == "classes":
            self.classes = CLASSES
            self.perform_filter = classes_filter
        elif type == "research":
            self.research_topics = RESEARCH_TOPICS
            self.perform_filter = research_filter
        elif type == "interests":
            self.perform_filter = interest_filter


def time_filter(self, student, professors):
    #still needs to be implemented

def department_filter(self, student, professors):
    result = []
    for professor in professors:
        if professor.deparment in self.deparments:
            result.append(professors)
    return result

def classes_filter(self, student, professors):
    result = []
    for professor in professors:
        if professor.classes_teaching in self.classes:
            result.append(professor)
    return result

def research_filter(self, student, professors):
    result = []
    for professor in professors:
        for topic in professor.research_topics:
            if topic in self.research_topics and professor not in results:
                result.append(professor)
    return result

def interest_filter(self, student, professors):
    result = []
    for professor in professors:
        for interest in professors.interests:
            if interest in student.interests and professor not in result:
                result.append(professor)
    return result
