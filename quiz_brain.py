class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_q.text} (True/False?): ").capitalize()
        if answer == current_q.answer:
            self.score += 1
            print(f"You got it the correct answer was {current_q.answer}")

        else:
            print(f"You were wrong, the correct answer {current_q.answer}")
        print(f"You current score is {self.score}/{self.question_number}")
        print("\n")



