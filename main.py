THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
import  data


class window:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.config(padx=100, pady=100, bg=THEME_COLOR)

        self.score = Label(text="SCORE : 0",fg="white", bg=THEME_COLOR, font=("arial", 20, "normal"))
        self.score.grid(column=2,row=0)

        self.canvas = Canvas(width=600,height=400)
        self.canvas.grid(column=1, row=1, columnspan=2, pady=100)

        self.text = self.canvas.create_text(300,200,width=500, text="Somthing", font=("arial", 20, "bold"))

        self.false = PhotoImage(file="false.png")
        self.wrong_button = Button(image= self.false,command=self.wrong_ans)
        self.wrong_button.grid(column=1, row=3)

        self.right = PhotoImage(file="true.png")
        self.right_button = Button(image=self.right, command=self.right_ans)
        self.right_button.grid(column=2, row=3)
        self.question()

        self.screen.mainloop()

    def question(self):
            if self.quiz.still_has_questions():
                self.canvas.config(bg="white")
                self.que = self.quiz.next_question()
                self.canvas.itemconfig(self.text, text= self.que)
            else:
                self.canvas.config(bg="white")
                self.canvas.itemconfig(self.text, text="you have done")
                self.right_button.st
    def right_ans(self):
        self.feedback(self.quiz.check_answer("true"))


    def wrong_ans(self):
       self.feedback(self.quiz.check_answer("false"))

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score.config(text=f"score: {self.quiz.score}")
        else:
            self.canvas.config(bg="red")
        self.screen.after(1000, self.question)

