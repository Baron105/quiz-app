from tkinter import *
from tkinter import messagebox as mb
import json
import html
import requests
from random import shuffle

def fetch_questions(amount=4, category=9, difficulty='easy', question_type='multiple'):
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}&difficulty={difficulty}&type={question_type}"
    response = requests.get(url)
    data = response.json()

    questions = []
    options = []
    answer = []

    for question in data['results']:
        questions.append(question['question'])
        incorrect_answers = question['incorrect_answers']
        correct_answer = question['correct_answer']
        all_answers = incorrect_answers + [correct_answer]
        shuffle(all_answers)
        options.append(all_answers)
        answer.append(all_answers.index(correct_answer) + 1)

    quiz_data = {
        'question': questions,
        'options': options,
        'answer': answer
    }

    with open('data.json', 'w') as file:
        json.dump(quiz_data, file, indent=4)

class GUI:
    def __init__(self):
        self.question_number = 0
        self.display_title()
        
        self.option_selected = IntVar()
        self.options = self.radio_buttons()
        self.display_question()
        self.display_options()
        
        self.buttons()
        self.total_questions = len(question)
        self.correct = 0
        
    def display_result(self):
        correct = f"Correct: {self.correct}"
        incorrect = f"Incorrect: {self.total_questions - self.correct}"
        
        score = int(self.correct / self.total_questions * 100)
        result = f"Score: {score}%"
        
        mb.showinfo("Result", f"{result}\n{correct}\n{incorrect}")
        
    def check_answer(self, question_number):
        if self.option_selected.get() == answer[question_number]:
            return True
        
    def next_button(self):
        if self.check_answer(self.question_number):
            self.correct += 1
            
        self.question_number += 1
        
        if self.question_number == self.total_questions:
            self.display_result()
            gui.destroy()
            
        else:
            self.display_question()
            self.display_options()
            
    def buttons(self):
        button_frame = Frame(gui)
        button_frame.pack(side=BOTTOM, pady=10)
        
        next_button = Button(button_frame, text="Next", command=self.next_button)
        next_button.pack(side=LEFT, padx=20)
        
        quit_button = Button(button_frame, text="Quit", command=gui.destroy)
        quit_button.pack(side=RIGHT, padx=20)
        
    def display_options(self):
        val = 0
        self.option_selected.set(0)
        
        for option, radio_btn in zip(options[self.question_number], self.options):
            radio_btn.configure(text=html.unescape(option))
            val += 1
    
    def display_question(self):
        for widget in gui.winfo_children():
            if isinstance(widget, Label):
                widget.destroy()
        
        question_label = Label(gui, text=html.unescape(question[self.question_number]))
        question_label.pack(side=TOP)
        
        
    def display_title(self):
        title = Label(gui, text="Quiz")
        title.pack(side=TOP)
        
    def radio_buttons(self):
        q_list = []
        
        y_pos = 50
        
        while len(q_list) < 4:
            radio_btn = Radiobutton(gui, text=" ", variable=self.option_selected, value=len(q_list) + 1)
            q_list.append(radio_btn)
            radio_btn.pack(side=TOP, ipady=5)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 25
            
        return q_list
    
gui = Tk()
gui.geometry("750x250")
gui.title("Quiz")

fetch_questions(amount=4, category=9, difficulty='easy', question_type='multiple')
with open('data.json') as f:
    data = json.load(f)
    
question = (data['question'])
options = (data['options'])
answer = (data['answer'])

quiz = GUI()
gui.mainloop()