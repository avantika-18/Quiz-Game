import tkinter as tk
from tkinter import *
from tkinter import ttk
from QuizLib import *
import random

# Functionality Related: This function takes the answer selected by the users and the correct answer \
# and increments the quiz score


def get_score(Answer, radiolist):
    global QuizScore
    if Answer == radiolist:
        QuizScore = QuizScore + 1
    return QuizScore

# Windows Related: This function displays the quiz answers in a new window


def showAnswers(window, rand_question_nos: list):
    window.withdraw()
    aWindow = Toplevel()
    aWindow.geometry("420x420")
    aWindow.title("Quiz / Answers")
    aWindow.config(background="Dark cyan")
    f = open(chosenSubject.get() + "_answers.txt", "r")
    print("f is", f)
    lines = f.readlines()
    count = 0

    Label(aWindow, text="Correct answers for your questions", font=('Calibri', 11, 'bold'), fg='purple', bg='dark cyan', anchor="w", wraplength=350,
          justify=LEFT).pack()

    for qno in rand_question_nos:
        l=lines[qno]
        print(lines[qno])
        if (count >= 0) and (count < 7):
            Label(aWindow, text=l, font=('Calibri', 11, 'bold'), fg='purple', bg='dark cyan', anchor="w", wraplength=350,
                  justify=LEFT).pack()
        count += 1
    Button(aWindow, text="Back to Main Screen", font=('Arial', 8, 'bold'), fg='purple', bg='dark cyan',
           command=lambda: mainscreen(aWindow)).pack()

# Windows Related: This function displays the main screen


def mainscreen(windowName):
    windowName.destroy()
    root.deiconify()


# Windows Related: This function contains all the functionality \
# of the quiz questions pages

def quizPage():
    root.withdraw()
    global QuizScore
    QuizScore=0
    window = Toplevel(root)
    window.geometry("420x420")
    window.title("Quiz")
    window.config(background="Dark cyan")
    Label(window, text="Questions for you", font=('Arial', 50, 'bold'), fg='purple', bg='dark cyan')
    subject = chosenSubject.get()
    print("subject is", subject)
    result = get_the_sentences(subject + ".txt")
    count = 0
    label1=Label(window, text="")
    countVar = tk.IntVar()
    no_of_questions= len(result)
    rand_question_nos= random.sample(range(no_of_questions), 5)
    print("random qns are", rand_question_nos)
    for qn in rand_question_nos:
        l=result[qn]
        print(result[qn])

        options=get_the_question(l, 2, -1)
        qno=get_question_no(l)
        print("qno is", qno)
        print("options are ", options)

        if (count >= 0) and (count < 7):
            v = tk.StringVar()
            joined_line=''
            # label1.destroy()
            joined_line='\n'.join(get_the_question(l,0,2))

            joined_line=joined_line+ "\n"+ "\n"+ "Choose from the following options" +"\n"
            print("joined line is ", joined_line)
            label1= Label(window, text=joined_line, font=('Calibri', 11, 'bold'), fg='purple', bg='dark cyan', anchor="w", wraplength=350,justify=LEFT)
            label1.pack()
            rblist=[]
            selectedvalue = StringVar()
            radiolist=[]
            for radiobuttonvalue in options:
                ind= options.index(radiobuttonvalue)
                # rb="w"+str(ind)
                rb = Radiobutton(window, text=radiobuttonvalue, anchor=W, variable=selectedvalue, value=radiobuttonvalue,font=('Calibri', 11, 'bold'), fg='purple', bg='dark cyan', justify=LEFT)
                selectedvalue.set(None)
                rblist.append(rb)
                #print("radio is ", selectedvalue.get())
                rb.pack(ipadx=0, ipady=10)
                radiolist.append(selectedvalue.get())

            button=Button(window, text="Next", command=lambda: get_score_and_destroy_widgets(countVar, label1, rblist, button, subject,qno, selectedvalue.get()))
            button.pack(ipadx=10, ipady=10, expand=True)
            button.wait_variable(countVar)

        count += 1
    print("QuizScore is", QuizScore)
    label2 = Label(window, text="In the subject "+subject+", "+quiztext(QuizScore), font=('Calibri', 11, 'bold'), fg='purple', \
                   bg='dark cyan', anchor="w",pady=20, wraplength=350, justify=LEFT)
    label2.pack()
    Button(window, text="Show Answers", font=('Arial', 8, 'bold'), fg='purple', bg='dark cyan',\
    command=lambda: showAnswers(window, rand_question_nos)).pack()


# Windows Related: This function takes the event of combo box changes and \
# binds the selected value changes


def subject_changed(event):
    """ handle the subject changed event """
    subject = chosenSubject.get()

# Windows Related: This function destroys the root window


def QuitApp():
    root.destroy()

# Windows Related: This function increments the quiz score by calling get_score function and \
# and destroys all the widgets that are passed as arguments


def get_score_and_destroy_widgets(countVar, label1, radiobutton, button, subject, qno, radiolist):
    button.destroy()
    global QuizScore
    Answer=get_the_answer(subject, qno)
    QuizScore=get_score(Answer, radiolist)

    for rb in radiobutton:
        rb.destroy()
    label1.destroy()
    countVar.set(1)
    return

# All the main part of the window which launches the quiz


root = tk.Tk()
root.geometry("420x420")
root.title("QUIZ GAME")
root.config(background="Dark cyan")
label = Label(root, text="QUIZ", font=('Arial', 50, 'bold'), fg='purple', bg='dark cyan')
label.pack()

label1 = Label(root, text="Please choose your subject below", font=('Calibri', 11, 'bold'), fg='purple', bg='dark cyan')
label1.pack()

f = open("modules.txt",  "r")
Subjects = f.read().splitlines()
print("subjects are", Subjects)
chosenSubject = StringVar()
subjectCB = ttk.Combobox(root, textvariable=chosenSubject)
subjectCB['values'] = Subjects
# prevent typing a value
subjectCB['state'] = 'readonly'
subjectCB.current(0)
subjectCB.pack(pady=20)
subjectCB.bind('<<ComboboxSelected>>', subject_changed)

print(subject_changed)

QuizButton = Button(root, text="Play", state=ACTIVE, padx=50, fg="blue", bg="white", command=quizPage)
QuizButton.pack()

myButton = Button(root, text="Quit", state=ACTIVE, padx=50, fg="blue", bg="white", command=QuitApp)
myButton.pack()
root.mainloop()


