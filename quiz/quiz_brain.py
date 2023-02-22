class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def next_question(self):
        while self.question_number < len(self.question_list):
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
            self.verify_answer(answer, current_question.answer)
            
    def verify_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print('Correct!')
            print(f'The correct answer is: {correct_answer}')
        else:
            print('Incorrect.')
            print(f'The correct answer is: {correct_answer}')
        print(f'Your current score is: {self.score}/{self.question_number}' )
        