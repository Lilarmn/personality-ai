from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter as tk
from cv2 import destroyAllWindows,imshow,waitKey,rectangle
import numpy as np 
import pickle
import mysql.connector as mc

# Main Window : 
model=pickle.load(open("aiEngine.sav","rb"))
root=tk.Tk()
root.title("Is he/she a good person?")
root.resizable(False,False)
root.geometry("800x900")
root.config(background='#708090')
# -----------------------
header=ttk.Label(root,
                 text="Bad Finder:",
                foreground='white',
                background='#708095',
                font=(None,30))
header.pack()
def CommandStart():
    showinfo(
        title='hint',
        message='please just put 0 for No and 1 for Yes'
    )
start=ttk.Button(root,
                text='Start',
                command=lambda : CommandStart())
start.pack(ipadx=50,pady=20)
Q1=ttk.Label(root,
                 text="Selfish?",
                foreground='white',
                background='#708095',
                font=(None,15))
Q1.pack(pady=10)
q1Answer=tk.IntVar()
q1Inp=ttk.Entry(root,
               textvariable=q1Answer,
               font=(None,15))
q1Inp.focus()
q1Inp.pack()

Q2=ttk.Label(root,
                 text="Attention?",
                foreground='white',
                background='#708095',
                font=(None,15))
Q2.pack(pady=10)
q2Answer=tk.IntVar()
q2Inp=ttk.Entry(root,
               textvariable=q2Answer,
               font=(None,15))
q2Inp.focus()
q2Inp.pack()

Q3=ttk.Label(root,
                 text="H***y?",
                foreground='white',
                background='#708095',
                font=(None,15))
Q3.pack(pady=10)
q3Answer=tk.IntVar()
q3Inp=ttk.Entry(root,
               textvariable=q3Answer,
               font=(None,15))
q3Inp.focus()
q3Inp.pack()

Q4=ttk.Label(root,
                 text="Does he\she Spend a lot of time with friends?",
                foreground='white',
                background='#708095',
                font=(None,15))
Q4.pack(pady=20)
q4Answer=tk.IntVar()
q4Inp=ttk.Entry(root,
               textvariable=q4Answer,
               font=(None,15))
q4Inp.focus()
q4Inp.pack()

Q5=ttk.Label(root,
                 text="MFGSH?",
                foreground='white',
                background='#708095',
                font=(None,15))
Q5.pack(pady=10)
q5Answer=tk.IntVar()
q5Inp=ttk.Entry(root,
               textvariable=q5Answer,
               font=(None,15))
q5Inp.focus()
q5Inp.pack()

Q6=ttk.Label(root,
                 text="Family Strict?",
                foreground='white',
                background='#708095',
                font=(None,15))
Q6.pack(pady=10)
q6Answer=tk.IntVar()
q6Inp=ttk.Entry(root,
               textvariable=q6Answer,
               font=(None,15))
q6Inp.focus()
q6Inp.pack()

Q7=ttk.Label(root,
                 text="Beauty?",
                foreground='white',
                background='#708095',
                font=(None,15))
Q7.pack(pady=10)
q7Answer=tk.IntVar()
q7Inp=ttk.Entry(root,
               textvariable=q7Answer,
               font=(None,15))
q7Inp.focus()
q7Inp.pack()


lashi='lashi'
salem='salem'
changeres=ttk.Label(root,text='Result :',
                    foreground='#708095',
                background='white',
                font=(None,25))
changeres.pack(pady=50)

def CommandResult(arr):
    global lashi
    global salem
    final=model.predict([arr])
    if  final==1:
        changeres.config(text='lashi')
    else:
        changeres.config(text='salem')
        
showresult=ttk.Button(root,
                text='Show Result',
                command=lambda : CommandResult(np.array([q1Answer.get(),q2Answer.get(),q3Answer.get(),
         q4Answer.get(),q5Answer.get(),q6Answer.get(),q7Answer.get()])))
showresult.pack(expand=True)

def resetInputs():
    list_inputs=[q1Inp,q2Inp,q3Inp,q4Inp,q5Inp,q6Inp,q7Inp]
    for inp in list_inputs:
        inp.delete(0,tk.END)

resetButton=tk.Button(root,
            text='reset',
            command=lambda : resetInputs(),
            )
resetButton.pack(expand=True)

# -----------------------
try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()