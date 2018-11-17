from filters import *

class User:
    def __init__(self, calendar):
        self.calendar = calendar

class Student(User):
    def __init__(self, calendar, name, classes, interests, filters):
        self.name = name
        self.classes = classes
        self.interests = interests
        self.filters = filters
        User.__init__(self, calendar)

    def recommend_algorithm(self, professors):
        result = professors[:]
        for filter in self.filters:
            result = filter.perform_filter(self, result)
        return result

    def to_dictionary(self):
        return {"Name": self.name, "Major":self.major, "Year":self.year, "Classes":self.classes, "Calendar":self.calendar}

class Professor(User):
    def __init__(self, calendar, name, department, classes_teaching, research_topics, interests, bio, email, website):
        self.name = name
        self.department = department
        self.classes_teaching = classes_teaching
        self.research_topics = research_topics
        self.interests = interests
        self.bio = bio
        self.email = email
        self.website = website
        User.__init__(self, calendar)
    def to_dictionary(self):
        return {"Name": self.name, "Department":self.department, "Classes":self.classes_teaching, "Research Topics":self.research_topics,
                "Interests":self.interests, "Bio":self.bio, "Email":self.email, "Website":self.website,
                "Calendar":self.calendar}
