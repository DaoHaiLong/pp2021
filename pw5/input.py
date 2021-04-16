import math
import curses
import numpy as np
from domain.Student import *
from domain.Course import *
from domain.Mark import *

py = curses.initscr() 
curses.start_color()


class inputs():
     
     def input_number_student():
         while True:
             py.refresh()
             Num=int(py.getstr().decode())
             if Num <=0:
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                py.addstr("Does not exits!!!\n", curses.color_pair(1))
                py.refresh()
                curses.napms(3000)
                py.clear()
                py.refresh()
             else:
                 return Num
             
         
     def input_number_course():
         while True:
             py.refresh()
             Nco=int(py.getstr().decode())
             if Nco<=0:
                 curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                 py.addstr("Does not exits!!!\n", curses.color_pair(1))
                 py.refresh()
                 curses.napms(3000)
                 py.clear()
                 py.refresh()
             else:
                 return Nco
             
     def inputstudent():
         py.addstr("Enter StudentID:")
         py.refresh()
         id=py.getstr().decode()
         StudentID.append(id)
    
         py.addstr("Enter StudentName:")
         py.refresh()
         name=py.getstr().decode()
         StudentName.append(name)
         
         py.addstr("Enter date of brith:")
         py.refresh()
         dob=py.getstr().decode()
         Studentdob.append(dob)
         if len(Students) == 0:
                f = open("students.txt", "w")
         else:
                f = open("students.txt", "a")
         f.write(id + "\n" + name + "\n" + dob + "\n")
         f.close()
         Student(id,name,dob)
         
         
    
     def inputCourses():
         py.addstr("Enter CourseID:")
         py.refresh()
         cid=py.getstr().decode()
         CoursesID.append(cid)
         
         py.addstr("Enter CourseName:")
         py.refresh()
         name=py.getstr().decode()
         CoursesName.append(name)
         
         py.addstr("Enter CourseCredit:")
         py.refresh()
         credit=float(py.getstr().decode())
         Courses_credit.append(credit)
         if len(Courses) == 0:
                f = open("courses.txt", "w")
         else:
                f = open("courses.txt", "a")
        
         f.write(cid + "\n" + name + "\n" + str(credit) + "\n")
         f.close()
         Course(cid,name,credit)
         
         
     def inputmark():
         py.addstr("- Enter the courseID you want to input mark: ")
         cid = py.getstr().decode()
         py.clear()
         py.refresh()
         if cid in CoursesID:
            py.addstr("- Enter the StudentID you want to input mark: ")
            id=py.getstr().decode()
            py.clear()
            py.refresh()
            if id in StudentID:   
                while True:           
                     py.addstr(" input mark of this student in courses: ")
                     marks=math.floor(float(py.getstr().decode()))
                     if marks<0 or marks>20:
                        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                        py.addstr("error,enter again!\n", curses.color_pair(1))
                        py.refresh()
                        curses.napms(500)
                        py.clear()
                        py.refresh()
                        py.addstr("Press any number: ")
                        marks=math.floor(float(py.getstr().decode()))
                     else:
                         break  
            else:
                exit()
         else:
             exit() 
         if len(Mark) == 0:
                f = open("marks.txt", "w")
         else:
                f = open("marks.txt", "a")
         f.write(id + "\n" + cid + "\n" + str(marks) + "\n")
         f.close()
         Mark_marks.append(marks)
         Marks(cid,id,marks)
         
#------------------------------------------- func calc gpa -------------------------------------------#   

     def Gpa():
         #  If Number courses> = 2 then to calculate the gpa of a student we must enter the correct student id #
         
            value=np.array([Mark_marks])
            cre=np.array([Courses_credit])
            py.addstr("enter student id you want to calculate gpa:")
            id =py.getstr().decode()
            if id in StudentID:
                for i in range(0,len(Mark)):
                     totalCredit=np.sum(cre)
                     totalValue=np.sum(np.multiply(value,cre))
                     gpa=totalValue/totalCredit
            else: 
                return 0
            Mark_gpa.append(gpa)
            for mark in Mark:
                 py.addstr(" [Mark_studentid: ] %s   [Gpa: ]%s \n" %(mark.get_id(),gpa))
                 py.refresh()
                 break
                 
    
    