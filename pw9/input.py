
import math
import curses
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import *

from domain.Student import *
from domain.Course import *
from domain.Mark import *

py = curses.initscr() 
curses.start_color()

class inputs():
     
    def input_number_Student():
        root = Tk()
        root.title('Number of student')
        root.geometry("280x100")

        mainframe = Frame(root)
        mainframe.grid()

        Num_var = StringVar()
        lbl_numStu = Label(mainframe, font=('arial', 10), text="Number_Student", padx=10, pady=10)
        lbl_numStu.grid(row=0, column=0)
        txt_numStu = Entry(mainframe, font=('arial', 10), width=20, textvariable=Num_var)
        txt_numStu.grid(row=0, column=1, padx=2)
        
        def NumSTU():
            try:
                Num = int(txt_numStu.get())
                if Num <= 0:
                    messagebox.showerror(message="Error: number of students must be non-negative")
                    txt_numStu.delete(0, END)
                else:
                    Num = int(txt_numStu.get())
                    root.destroy()
            except:
                messagebox.showerror(message="Invalid number of student")

       
                

        btnSTU = Button(mainframe,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        width=10,
                        height=3,
                        text='OK',
                        command=NumSTU)

        btnSTU.grid(row=1,column=1,padx=1)
             
         
    def input_number_Courses():
        root1 = Tk()
        root1.title('Number of Courses')
        root1.geometry("280x100")

        mainframe1 = Frame(root1)
        mainframe1.grid()

        Nco_var = StringVar()
        lbl_numCOU = Label(mainframe1, font=('arial', 10), text="Number_Courses", padx=10, pady=10)
        lbl_numCOU.grid(row=0, column=0)
        txt_numCOU = Entry(mainframe1, font=('arial', 10), width=20, textvariable=Nco_var)
        txt_numCOU.grid(row=0, column=1, padx=2)
        def NumCOU():
            try:
                Nco = int(txt_numCOU.get())
                if Nco <= 0:
                    messagebox.showerror(message="Error: number of students must be non-negative")
                    txt_numCOU.delete(0, END)
                else:
                      Nco = int(txt_numCOU.get())
                      root1.destroy()
            except:
                messagebox.showerror(message="Invalid number of student")

        btnCOU = Button(mainframe1,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        width=10,
                        height=3,
                        text='OK',
                        command=NumCOU)

        btnCOU.grid(row=1,column=1,padx=1)
             
    def inputstudent():
        stu = Tk()
        stu.title('Information Student')
        stu.geometry("280x200")
        
        mainframe2 = Frame(stu)
        mainframe2.grid()
        
        id_var=StringVar()
        lbl_stuId = Label(mainframe2, font=('arial', 10), text="Id", padx=10, pady=10)
        lbl_stuId.grid(row=0, column=0)
        txt_stuId = Entry(mainframe2, font=('arial', 10), width=20, textvariable=id_var)
        txt_stuId.grid(row=0, column=1, padx=2,sticky="w")
        txt_stuId.focus_set()
        
        name_var=StringVar()
        lbl_stuName = Label(mainframe2, font=('arial', 10), text="Name", padx=10, pady=10)
        lbl_stuName.grid(row=1, column=0)
        txt_stuName = Entry(mainframe2, font=('arial', 10), width=20, textvariable=name_var)
        txt_stuName.grid(row=1, column=1, padx=2,sticky="w")
        txt_stuName.focus_set()
        
        dob_var=StringVar()
        lbl_studob = Label(mainframe2, font=('arial', 10), text="DOB", padx=10, pady=10)
        lbl_studob.grid(row=2, column=0)
        txt_studob = Entry(mainframe2, font=('arial', 10), width=20, textvariable=dob_var)
        txt_studob.grid(row=2, column=1, padx=2,sticky="w")
        txt_studob.focus_set()
        def Stu():
                id=txt_stuId.get()
                name=txt_stuName.get()
                dob=txt_studob.get()
                if id=="":
                    messagebox.showerror(message="Error: Student ID  be empty")
                elif name=="":
                    messagebox.showerror(message="Error: Student Name  be empty")
                elif dob=="":
                    messagebox.showerror(message="Error: Student dob  be empty")
                else:
                    StudentID.append(id)
                    StudentName.append(name)
                    Studentdob.append(dob)
                    Student(id,name,dob)
                    messagebox.showinfo(message="Successfully added students")
                    stu.destroy()
            
        btnStudent = Button(mainframe2,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        width=10,
                        height=3,
                        text='ADD',
                        command=Stu)

        btnStudent.grid(row=4,column=1,padx=1)

                
            
    def inputCourses():
        cou = Tk()
        cou.title('Information course')
        cou.geometry("280x200")
        
        mainframe3 = Frame(cou)
        mainframe3.grid()
        
        cid_var=StringVar()
        lbl_couId = Label(mainframe3, font=('arial', 10), text="CId", padx=10, pady=10)
        lbl_couId.grid(row=0, column=0)
        txt_couId = Entry(mainframe3, font=('arial', 10), width=20, textvariable=cid_var)
        txt_couId.grid(row=0, column=1, padx=2,sticky="w")
        txt_couId.focus_set()
        
        name_var=StringVar()
        lbl_couName = Label(mainframe3, font=('arial', 10), text="Name", padx=10, pady=10)
        lbl_couName.grid(row=1, column=0)
        txt_couName = Entry(mainframe3, font=('arial', 10), width=20, textvariable=name_var)
        txt_couName.grid(row=1, column=1, padx=2,sticky="w")
        txt_couName.focus_set()
        
        credit_var=StringVar()
        lbl_coucredit = Label(mainframe3, font=('arial', 10), text="Credit", padx=10, pady=10)
        lbl_coucredit.grid(row=2, column=0)
        txt_coucredit = Entry(mainframe3, font=('arial', 10), width=20, textvariable=credit_var)
        txt_coucredit.grid(row=2, column=1, padx=2,sticky="w")
        txt_coucredit.focus_set()
        def Cou():
            cid=txt_couId.get()
            name=txt_couName.get()
            credit=txt_coucredit.get()
            if cid=="":
                    messagebox.showerror(message="Error: Courses ID  be empty")
            elif cid=="":
                messagebox.showerror(message="Error: Courses Name  be empty")
            elif cid=="":
                messagebox.showerror(message="Error: Courses credit  be empty")
            else:
                CoursesID.append(cid)
                CoursesName.append(name)
                Courses_credit.append(credit)
                Course(cid,name,credit)
                messagebox.showinfo(message="Successfully added Courses ")
                cou.destroy()
            
        btncoures = Button(mainframe3,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        width=10,
                        height=3,
                        text='ADD',
                        command=Cou)

        btncoures.grid(row=4,column=1,padx=1)
         
         
    def inputmark():
        mar = Tk()
        mar.title('Information mark')
        mar.geometry("280x200")
        
        mainframe4 = Frame(mar)
        mainframe4.grid()
        
        cid_var=StringVar()
        lbl_couId = Label(mainframe4, font=('arial', 10), text="Course Id", padx=10, pady=10)
        lbl_couId.grid(row=0, column=0)
        txt_couId = Entry(mainframe4, font=('arial', 10), width=20, textvariable=cid_var)
        txt_couId.grid(row=0, column=1, padx=2,sticky="w")
        txt_couId.focus_set()
        
        id_var=StringVar()
        lbl_stuId = Label(mainframe4, font=('arial', 10), text="Student Id", padx=10, pady=10)
        lbl_stuId.grid(row=1, column=0)
        txt_stuId = Entry(mainframe4, font=('arial', 10), width=20, textvariable=id_var)
        txt_stuId.grid(row=1, column=1, padx=2,sticky="w")
        txt_stuId.focus_set()
        
        marks_var=StringVar()
        lbl_marks = Label(mainframe4, font=('arial', 10), text="Mark", padx=10, pady=10)
        lbl_marks.grid(row=2, column=0)
        txt_marks = Entry(mainframe4, font=('arial', 10), width=20, textvariable=marks_var)
        txt_marks.grid(row=2, column=1, padx=2,sticky="w")
        txt_marks.focus_set()
        def Mar():
            cid=txt_couId.get()
            if (cid=="") or (cid  not in CoursesID):
                    messagebox.showerror(message="Error: Courses ID  be empty")
            elif cid in CoursesID:
                id=txt_stuId.get()
                if (id=="") or (id  not in StudentID):
                    messagebox.showerror(message="Error: Student ID  be empty")
                elif id in StudentID:
                    marks=math.floor(txt_marks.get())
                    if marks<0 or marks >20:
                        messagebox.showerror(message="Error: mark aren't exit")
                    else:
                        marks=math.floor(txt_marks.get())
                        Mark_marks.append(marks)
                        Marks(cid,id,marks)
                        mar.destroy()
        btnMark = Button(mainframe4,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        width=10,
                        height=3,
                        text='ADD',
                        command=Mar)

        btnMark.grid(row=4,column=1,padx=1)
                    
         
#------------------------------------------- func calc gpa -------------------------------------------#   

    def Gpa():
         #  If Number courses> = 2 then to calculate the gpa of a student we must enter the correct student id #
        margrad = Tk()
        margrad.title('Information Gpa')
        margrad.geometry("280x150")
        
        mainframe5 = Frame(margrad)
        mainframe5.grid()
        value=np.array([Mark_marks])
        cre=np.array([Courses_credit])
        
        id_var=StringVar()
        lbl_stuId = Label(mainframe5, font=('arial', 10), text="Student Id", padx=10, pady=10)
        lbl_stuId.grid(row=0, column=0)
        txt_stuId = Entry(mainframe5, font=('arial', 10), width=20, textvariable=id_var)
        txt_stuId.grid(row=0, column=1, padx=2,sticky="w")
        txt_stuId.focus_set()
        def cal():
            id=txt_stuId.get()
            if (id=="") or (id  not in StudentID):
                messagebox.showerror(message="Error: Student ID  be empty")
                
            elif id in StudentID:
                for i in range(0,len(Mark)):
                    totalCredit=np.sum(cre)
                    totalValue=np.sum(np.multiply(value,cre))
                gpa=totalValue/totalCredit
            else: 
                messagebox.showerror(message="Error: Courses ID  be empty")
            Mark_gpa.append(gpa)
            margrad.destroy()
        btngpa= Button(mainframe5,
                        fg="red",
                        font=('arial', 9, 'bold'),
                        width=10,
                        height=3,
                        text='Calc',
                        command=cal)

        btngpa.grid(row=1,column=1,padx=1)
            
            
                    
    
    