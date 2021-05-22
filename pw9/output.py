
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *
import tkinter as tk
from tkinter import messagebox
from tkinter import *



class outputs():
    def ShowCourses():
        root = Tk()
        root.title('Coures')
        root.geometry("400x200")
        
        mainframe = Frame(root)
        mainframe.grid()
        
        lbl1=Label(mainframe,text="Course list")
        lbl1.grid(row=0,column=0)
        for courses in Courses:
            lblcourse=Label(mainframe,text=" [cid: ] %s  [Name: ] %s   [credit: ] %s \n" % (courses.get_cid(), courses.get_name(), courses.get_credit()))
            lblcourse.grid(row=(Courses.index(courses) + 1), column=0)

    def ShowStudent():
        root1 = Tk()
        root1.title('Student')
        root1.geometry("400x200")
        
        mainframe1 = Frame(root1)
        mainframe1.grid()
        
        lbl2=Label(mainframe1,text="Student list")
        lbl2.grid(row=0,column=0)
        for students in Students:
            lblstudents=Label(mainframe1,text=" [id: ] %s  [Name:] %s   [dob:] %s \n" % (students.get_id(), students.get_name(), students.get_dob()))
            lblstudents.grid(row=(Students.index(students) + 1), column=0)
            
            
    def ShowMarks():
        
        root2= Tk()
        root2.title('Mark')
        root2.geometry("400x200")
        
        mainframe2 = Frame(root2)
        mainframe2.grid()
        
        lbl3=Label(mainframe2,text="Mark list")
        lbl3.grid(row=0,column=0)
        for m in Mark:
            lblstudents=Label(mainframe2,text=" [Mark_coursesid: ] %s  [Mark_studentid: ] %s   [Mark_mark: ] %s \n" % (m.get_cid(), m.get_id(), m.get_marks()))
            lblstudents.grid(row=(Mark.index(m) + 1), column=0)
            
            
           
            
    def GPA_decending():
        root3= Tk()
        root3.title('GPA')
        root3.geometry("400x200")
        
        mainframe3 = Frame(root3)
        mainframe3.grid()
        
        lbl3=Label(mainframe3,text="GPA decending")
        lbl3.grid(row=0,column=0)
        
        arr=np.array([Mark_gpa])  
        arr[::-1].sort()
        lbl4=Label(mainframe3,text="The list after sorting is %s: \n" %(arr))
        lbl4.grid(row=0,column=0)
        
            
