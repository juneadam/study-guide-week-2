# Create your classes here
class Student:
    """Create objects of class Student, containing student names and addresses"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question:
    """Create Question objects containing a question and its correct answer"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_answer(self):
        response = input(self.question)
        if response == self.correct_answer:
            return True
        else:
            return False


class Exam:
    """Create Exam objects, containing a name and a list of Question objects"""

    questions = []

    def __init__(self, name):
        self.name = name

    def add_question(self, Question_obj):
        """Method to add individual question to the exam."""
        self.questions.append(Question_obj)
    
    def administer(self):
        tally = 0
        for question in self.questions:
            if question.ask_and_answer():
                tally += 1
        
        score = 100 * (tally / len(self.questions))
        print(f'Your final score is {score}')

        
