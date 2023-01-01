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
        return score


class Quiz(Exam):
    """subclass of exam, where score is modified for pass/fail"""    
    def administer(self):
        score = super().administer()
        if score >= 60.0:
            return 1
        else:
            return 0


class StudentExam:
    """object is a student exam, exam + method for administration"""
    score = 0

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
    
    def take_test(self):
        """uses the administer method to run and score the exam"""
        self.score = self.exam.administer()


class StudentQuiz:
    """object is a student quiz, quiz subclass of exam + method for administration"""
    score = 0

    def __init__(self, student, quiz):
        self.student = student
        self.quiz = quiz
    
    def take_test(self):
        """uses the administer method to run and score the exam"""
        self.score = self.quiz.administer()


def example():
    """creates a working student exam"""
    first_exam = Quiz('First Exam')
    alberta_capital = Question('What is the capital of Alberta?', 'Edmonton')
    first_exam.add_question(alberta_capital)
    python_author = Question('Who is the author of Python?', 'Guido Van Rossum')
    first_exam.add_question(python_author)
    set_q = Question('What is the method for adding an element to a set?', '.add()')
    first_exam.add_question(set_q)
    pwd_q = Question('What does pwd stand for?', 'print working directory')
    first_exam.add_question(pwd_q)
    list_q = Question('Python lists are mutable, iterable, and what?', 'ordered')
    first_exam.add_question(list_q)

    june = Student('June', 'Adam', '2023 Still here again')

    student_exam_1 = StudentQuiz(june, first_exam)

    student_exam_1.take_test()

    print(student_exam_1.score)

example()




