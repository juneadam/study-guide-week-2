# Create your classes here
class Student:

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question:

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

class Exam:

    questions = []

    def __init__(self, name):
        self.name = name

    def add_question(self, Question_obj):
        self.questions.append(Question_obj)