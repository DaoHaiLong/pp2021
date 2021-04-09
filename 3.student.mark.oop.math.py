
# Student management

import math
import numpy as np
import curses

#------------------------------------list-----------------------------------#

Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Courses_credit=[]
Mark=[]
Mark_marks=[]
Mark_gpa=[]


#-----------------------------------Student-----------------------------#

py = curses.initscr() 
curses.start_color()

class  Student:
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
        Students.append(self) 
        StudentID.append(self.id)
        
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob
    
     
#-------------------------------------Course----------------------------------------#

class Course:
    def __init__(self,cid,name,credit):
        self.cid=cid
        self.name=name
        self.credit=credit
        Courses.append(self)
        CoursesID.append(self.cid)
        Courses_credit.append(self.credit)
        
    def get_cid(self):
        return self.cid
    def get_name(self):
        return self.name
    def get_credit(self):
        return self.credit


#----------------------------------------Mark----------------------------------------#

class Marks:
    def __init__(self,cid,id,marks,gpa=0):
        self.cid=cid
        self.id=id
        self.marks=marks
        self.gpa=gpa
        Mark.append(self)
        Mark_marks.append(self.marks)
        
    def get_cid(self):
         return self.cid
    def get_id(self):
        return self.id
    def get_marks(self):
        return self.marks
    def get_gpa(self):
        return self.gpa
    def set_gpa(self,gpa):
        self.gpa=gpa

    
#------------------------------------------Show--------------------------------------# 

class main:
#-----------------------------------func input numbers courses,student---------------------------#

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
             
#-----------------------------------func input info courses,student---------------------------# 

     def inputstudent():
         py.addstr("Enter StudentID:")
         py.refresh()
         id=py.getstr().decode()
         
         py.addstr("Enter StudentName:")
         py.refresh()
         name=py.getstr().decode()
         
         py.addstr("Enter date of brith:")
         py.refresh()
         dob=py.getstr().decode()
         Student(id,name,dob)
         
    
     def inputCourses():
         py.addstr("Enter CourseID:")
         py.refresh()
         cid=py.getstr().decode()
         
         py.addstr("Enter CourseName:")
         py.refresh()
         name=py.getstr().decode()
         
         py.addstr("Enter CourseCredit:")
         py.refresh()
         credit=float(py.getstr().decode())
         Course(cid,name,credit)
         
         
     def inputmark():
         py.addstr("- Enter the courseID you want to input mark: ")
         cid = (py.getstr().decode())
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
                 
# -------------------------------------------------display function-------------------------------------------#
         
     def ShowCourses():
        py.addstr("Show lists of Courses:\n")
        py.refresh()
        for course in Courses:
            py.addstr("[CourseID: ] %s     [CourseName: ] %s     [CourseCredits: ] %s\n" % (course.get_cid(), course.get_name(), course.get_credit()))
            py.refresh()
            

     def ShowStudent():
         py.addstr("Show lists of student:\n")
         py.refresh()
         for student in Students:
            py.addstr("[Studentid: ] %s    [StudentName: ] %s     [StudentDOB: ] %s \n" % (student.get_id(), student.get_name(), student.get_dob()))
            py.refresh()
            
            
     def ShowMarks():
        py.addstr("Show lists of mark:\n")
        py.refresh()
        for mark in Mark:
            py.addstr("[Mark_coursesid: ] %s     [Mark_studentid: ] %s    [Mark_mark: ] %s\n" % (mark.get_cid(), mark.get_id(), mark.get_marks()))
            py.refresh()
            
     def GPA_decending():
            arr=np.array([Mark_gpa])  
            arr[::-1].sort()
            py.addstr("The list after sorting is %s: \n"%(arr))
            py.refresh()
            
                
            
     def displaycenteroutline(infomation):
            row,colum=py.getmaxyx()
            Xrow = int(row/ 3)
            Ycolumn = int(colum / 3)
            if infomation == "--- This is a Student management program ---":
                py.addstr(Xrow, Ycolumn , infomation,curses.A_BLINK)
                py.refresh()
            else:
                py.addstr(Xrow,Ycolumn,infomation, curses.A_BOLD)
                py.refresh()
    

#--------------------------------------------- Main func----------------------------------------------#

     def StudentManagement():  
         
      #-----------DISPLAY CENTER-------------------------------------------------#
         
         main.displaycenteroutline("---Hello friend---")
         py.refresh()
         curses.napms(1000)
         main.displaycenteroutline("This is a Student management program ")
         py.refresh()
         curses.napms(2000)
         py.clear()
         py.refresh()
        
    #------------------------- code running------------------------------------#
    
         py.addstr("\n 1 .Inputcourses information")
         py.addstr("\n 2 .Stop\n")
         py.addstr("You choose:  ")
         option=int(py.getstr().decode())
         py.refresh()
         while True:
             if option==1:
                 py.clear()
                 py.addstr("enter number of courses: ")
                 Nco=main.input_number_course()
                 py.clear()
                 py.refresh()
                 for i in range( Nco):
                     py.addstr(f"Course { i+1}\n")
                     main.inputCourses()
                     py.refresh()
                     py.addstr("enter number of student: ")
                     Num=main.input_number_student()
                     py.clear()
                     py.refresh()
                     for i in range(Num):
                         py.addstr(f"INPUT  STUDENT {i +1}:\n")
                         main.inputstudent()
                         py.clear()
                         py.refresh()
                         main.inputmark() 
                         py.clear()
                         py.refresh()   
                 break
             else:
                py.addstr("Good bye!")
                py.refresh()
                curses.napms(1000)
                curses.endwin()
                exit()        
         while True:
             py.addstr("1.Calculate and display gpa:\n")
             py.addstr("2.Show Student :\n")
             py.addstr("3.Show Courses :\n")
             py.addstr("4.Show Marks :\n")
             py.addstr("5.GPA_decending \n")
             py.addstr("6.Stop\n")
             py.addstr("You choose:  ")
             option1=int(py.getstr().decode())
             py.refresh()
             py.clear()
             py.refresh()
             if option1==1:
                 main.Gpa()
             if option1==2:
                 main.ShowStudent()
             if option1==3:
                 main.ShowCourses()
             if option1==4:
                 main.ShowMarks()
             if option1==5:
                 main.GPA_decending()
             elif option1==6:
                py.addstr("  Good bye,see you again\n  ")
                py.refresh()
                curses.napms(1000)
                curses.endwin()
                exit()  
                                                 
             
if __name__ == '__main__':
  
    main.StudentManagement()
    


