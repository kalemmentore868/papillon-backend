from fractions import Fraction
import random
from models.question_template import Question_Template


class Fraction_Template(Question_Template):
    def __init__(self, media, subject, question_id, description, difficulty, topic, subtopic, question_type, answer, csec_section, hint, status, name, question_text):
        super().__init__(media, subject, question_id, description, difficulty, topic,
                         subtopic, question_type, answer, csec_section, hint, status, name, question_text)

    def set_question_and_answer(self):
        # Creating two random fractions
        # Ensuring the denominator is not 1
        frac1 = Fraction(random.randint(1, 9), random.randint(2, 10))
        # Ensuring the denominator is not 1
        frac2 = Fraction(random.randint(1, 9), random.randint(2, 10))

        # Randomly choosing the symbol to be used
        symbol = ["+", "-", "x", "/"][random.randint(0, 3)]
        question = ""
        answer = ""

        # Creating the question and answer
        if symbol == "+":
            question = f"{frac1} + {frac2}"
            answer = frac1 + frac2
        elif symbol == "-":
            question = f"{frac1} - {frac2}"
            answer = frac1 - frac2
        elif symbol == "x":
            question = f"{frac1} x {frac2}"
            answer = frac1 * frac2
        elif symbol == "/":
            question = f"{frac1} / {frac2}"
            answer = frac1 / frac2

        self.question_text = question
        # Converting answer to string for ease of comparison later
        self.answer = str(answer)
