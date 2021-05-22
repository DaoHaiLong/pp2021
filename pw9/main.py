
import os
import curses
from output import outputs
from input import inputs
from domain.Student import *
from domain.Course import *
from domain.Mark import *
from brackground import BackgroundThreadobj
import tkinter as tk
from tkinter import messagebox
from tkinter import *

py = curses.initscr() 
curses.start_color()

def compress():
    with open('student.dat', 'wb') as zip:
        BackgroundThreadobj(pmo="dump",pdf=zip,pdum=len(Courses))   
        for course in Courses:
                BackgroundThreadobj(pmo="dump",pdf=zip,pdum=course)
            
        BackgroundThreadobj(pmo="dump",pdf=zip,pdum=len(Students))
        for student in Students:
            BackgroundThreadobj(pmo="dump",pdf=zip,pdum=student)
            
        BackgroundThreadobj(pmo="dump",pdf=zip,pdum=len(Mark))
        for mark in Mark:
            BackgroundThreadobj(pmo="dump",pdf=zip,pdum=mark)
            
def decompress():
    if os.path.isfile('student.dat'):
        with open('student.dat', 'rb') as zip:
            BackgroundThreadobj(pmo="load",pdf=zip,ploa=Num)
            for i in range(Num):
                BackgroundThreadobj(pmo="load",pdf=zip)
            BackgroundThreadobj(pmo="load",pdf=zip,ploa=Nco)
            for i in range(Nco):
                BackgroundThreadobj(pmo="load",pdf=zip)
            BackgroundThreadobj(pmo="load",pdf=zip,ploa=len(Mark))
            for i in range(len(Mark)):
                BackgroundThreadobj(pmo="load",pdf=zip)

def StudentManagement():
    
    root = Tk()
    root.title('Student Management')
    root.geometry("400x550")
    mainframe = Frame(root)
    mainframe.grid()
    lblmain=Label(mainframe,text='Student Management',font='arial')
    lblmain.grid(row=0,column=2,padx=100,pady=5)
    
    btn1=Button(text='Input_number_courses',command=inputs.input_number_Courses)
    btn1.grid(row=2,column=0,padx=5,pady=5)
    
    btn2=Button(text='Input Course',command=inputs.inputCourses)
    btn2.grid(row=3,column=0,padx=5,pady=5)
    
    btn2=Button(text='Input_number_student',command=inputs.input_number_Student)
    btn2.grid(row=4,column=0,padx=5,pady=5)
    
    btn3=Button(text='Input Student',command=inputs.inputstudent)
    btn3.grid(row=5,column=0,padx=5,pady=5)
    
    btn4=Button(text='Input Mark',command=inputs.inputmark)
    btn4.grid(row=6,column=0,padx=5,pady=5)
    
    btn7=Button(text='Calculation gpa ',command=inputs.Gpa)
    btn7.grid(row=7,column=0,padx=5,pady=5)
    
    btn5=Button(text='list Courses',command=outputs.ShowCourses)
    btn5.grid(row=8,column=0,padx=5,pady=5)
    
    btn6=Button(text='list Student',command=outputs.ShowStudent)
    btn6.grid(row=9,column=0,padx=5,pady=5)
    
    btn7=Button(text='list Mark',command=outputs.ShowMarks)
    btn7.grid(row=10,column=0,padx=5,pady=5)
    
    btn8=Button(text='GPA Decending',command=outputs.GPA_decending)
    btn8.grid(row=11,column=0,padx=5,pady=5)
    
    btn8=Button(text='Compress',command=compress)
    btn8.grid(row=12,column=0,padx=5,pady=5)
    
    btn9=Button(text='Decompress',command=decompress)
    btn9.grid(row=13,column=0,padx=5,pady=5)


    root.mainloop()
if __name__ == '__main__':
   
    StudentManagement()
    
