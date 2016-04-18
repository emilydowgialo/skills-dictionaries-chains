# Part 1

# 1. Abstraction: Hiding irrelevant data about an object to reduce complexity
#    and increase efficiency
#    Encapsulation: Everything is kept together. The inner workings of an object
#    can't be seen from the outside of its definition.
#    Polymorphism: Operations can be applied to values of some other type.

# 2. Classes describe how to make something, like a blueprint.

# 3. Instance attributes are owned by specific instances of a class.

# 4. A method is a function that belongs to an object.

# 5. An instance is a specific object, and its type is the class.

# 6. A class attribute is specific to the class, while an instance attribute
#    is owned by a specific instance of the class.

########################################################

# Part 2

# Student


# create a class Student
class Student(object):
    """this is the base class"""

    # each instance of class will be initialized using these parameters
    def __init__(self, name, last_name, address):
        """initialize address book entry"""

        self.name = name
        self.last_name = last_name
        self.address = address


# Question


# create a class Question
class Question(object):
    """this is the base class"""

    # each instance of Question will be initialized using these parameters
    def __init__(self, question, answer):
        """initialize question and answer"""

        self.question = question
        self.answer = answer


# Exam


# create a class Exam
class Exam(object):
    """this is the base class"""

    # each instance of Exam will be initialized using these parameters
    def __init__(self, name):
        """initialize exam"""
        self.questions = []
        self.name = name

#######################################################

# Part 3

# Part 3.1


class Exam(object):
    """this is the base class"""

    def __init__(self, name):
        """initialize exam"""
        self.questions = []
        self.name = name

    # this method takes a question and correct answer as parameters
    # and makes a question from these and adds the question to
    # the list of questions
    def add_question(self, question, correct_answer):
        """takes a question and answer and makes a question
        from them"""

        add_question = Question(question, correct_answer)

        # adds the question to the list
        self.questions.append(add_question)


# Part 3.2


class Question(object):
    """this is the base class"""

    def __init__(self, question, answer):
        """initialize address book entry"""

        self.question = question
        self.answer = answer

    # prints the question to the console and returns True or False
    # depending on if the user answers correctly
    def ask_and_evaluate(self):
        user_input = raw_input(self.question + " > ")
        if user_input == self.answer:
            return True
        else:
            return False


# Part 3.3


class Exam(object):
    """this is the base class"""

    def __init__(self, name):
        """initialize exam"""
        self.questions = []
        self.name = name

    def add_question(self, question, correct_answer):
        """takes a question and answer and makes a question
        from them"""

        add_question = Question(question, correct_answer)
        self.questions.append(add_question)

    # asks the user all the exam questions and increases the score by 1
    # for every right answer
    def administer(self):
        # score begins at 0, and increases by 1 per right answer
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                # increase the score by 1 if correct
                score += 1
        return score

########################################################

# Part 4


def take_test(exam, student):
    """will administer an exam and assign the score to the student"""

    # the score is returned by the administer method, which we call here
    score = exam.administer()

    # this assigns the score to the student instance as a new attribute, called
    # score
    student.score = score


def example():
    """this is an example exam, which creates an exam, with questions, creates a student, and administers the exam for the student"""

    # creates exam
    exam = Exam("Final")

    # adds questions to the exam
    exam.add_question("Do cats meow?", "yes")
    exam.add_question("Is it April?", "yes")

    # creates a student
    student = Student("Emily", "Smith", "123 Main St")

    # administers the test for the student
    take_test(exam, student)

########################################################

# Part 5


class Quiz(Exam):
    """this is the base class - it is a child of the Exam class; this will return True if the student passed the quiz, and False is the student did not pass"""

    # this is a child class, so it will inherit methods of the parent (Exam), 
    # but we need to override the administer method because it is unique to the
    # quiz class
    def administer(self):
        """returns True if student passed, and False if not"""

        # start score at 0, add 1 for a right answer
        score = 0

        # find the number of questions a student needs to pass (50% or above)
        number_of_questions = len(self.questions)
        needed_right = number_of_questions/float(2)

        # checks if a student answered a question correctly by calling
        # the question method 
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                score += 1

        # checks if the student answered the correct amount to pass the exam
        if score >= needed_right:
            # same as: score >= needed_right
            return True

        else:
            return False

##### BELOW THIS IS THE FINAL PRODUCT ALL IN ONE PLACE #####


class Student(object):
    """this is the base class"""

    def __init__(self, name, last_name, address):
        """initialize address book entry"""

        self.name = name
        self.last_name = last_name
        self.address = address


class Question(object):
    """this is the base class"""

    def __init__(self, question, answer):
        """initialize address book entry"""

        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        user_input = raw_input(self.question + " > ")
        return user_input == self.answer


class Exam(object):
    """this is the base class"""

    def __init__(self, name):
        """initialize exam"""

        self.questions = []
        self.name = name

    def question_and_answer(self, question, correct_answer):
        """takes a question and answer and makes a question
        from them"""

        question_with_answer = Question(question, correct_answer)
        self.questions.append(question_with_answer)

    def administer(self):
        score = 0
        for question in self.questions:
            if question.ask_and_evaluate() is True:
                score += 1
        return score


def take_test(exam, student):
    score = exam.administer()
    student.score = score


def example():
    exam = Exam("Final")
    exam.question_and_answer("Do cats meow?", "yes")
    exam.question_and_answer("Is it April?", "yes")
    student = Student("Emily", "Smith", "123 Main St")

    take_test(exam, student)


class Quiz(Exam):
    """this is the base class"""

    def administer(self):
        score = 0
        number_of_questions = len(self.questions)
        needed_right = number_of_questions/float(2)

        for question in self.questions:
            if question.ask_and_evaluate() is True:
                score += 1

        if score >= needed_right:
            return True

        else:
            return False






