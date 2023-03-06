from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUI:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = 'Quiz'
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=250, height=250)
        self.question_text = self.canvas.create_text(125,
                                                     125,
                                                     width=125,
                                                     text='Some Question Text',
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2)
        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.submit_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.submit_false)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text=f"Finished!\n\n{self.quiz.score}/10 Correct")
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def submit_true(self):
        self.is_correct(self.quiz.check_answer("True"))

    def submit_false(self):
        self.is_correct(self.quiz.check_answer("False"))

    def is_correct(self, correct):
        if correct:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
