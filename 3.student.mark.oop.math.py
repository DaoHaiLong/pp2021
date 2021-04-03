# Student management

import math
import numpy as np
#------------------------------------list-----------------------------------#
Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Mark=[]
MarkGPA=[]

#-----------------------------------Student-----------------------------#

class  Student:
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
        Students.append(self) 
        StudentID.append(self.id)
        
    def describe(self):
        print("id:            ",self.id,)
        print("name:          ",self.name,)    
        print("dob:           "  ,self.dob)
    
    def input_number_student():
        Num=int(input("Enter the numbers of Student:\n"))
        if Num <=0:
             print("Does not exist!!!")
             return 0
        else:
             return Num

    def inputStudent():
         print("Enter StudentID:")
         id=input()
         print("Enter StudentName:")
         name=input()
         print("Enter date of brith:")
         dob=input()
         Student(id,name,dob)

    
#-------------------------------------Course----------------------------------------#

class Course:
    def __init__(self,cid,name):
        self.cid=cid
        self.name=name
        Courses.append(self)
        CoursesID.append(self.cid)

    def describe(self):
        print("cid:        ",self.cid ,)
        print("name:       ", self.name)

    def input_number_courses():
         Nco=int(input("Enter the numbers of course:\n"))
         if Nco<=0:
            print("Does not exist!!!")
            return 0
         else:
             return Nco


    def inputCourses():
         print("Enter CoursesID:")
         cid=input()
         print("Enter CoursesName:")
         name=input()
         Course(cid,name)

#----------------------------------------Mark----------------------------------------#

class mark:
    def __init__(self,cid,id,marks,gpa):
        self.cid=cid
        self.id=id
        self.marks=marks
        self.gpa=gpa
        Mark.append(self)
        MarkGPA.append(self.gpa)
         
    def describe(self):
        print("Coursesid:       ", self.cid, )
        print("Studentid:       ", self.id, )
        print("mark:            ", self.marks,)
        print("gpa              ", self.gpa)
        
    
    def Mark_and_Gpa():
         print("Enter the Weighted of credits in this Course:")
         credits=float(input())
         print("Enter Coursesid you want to choose: ")
         cid=input()
         if cid in CoursesID:
             print("Enter StudentID you want to choose:")
             id=input()
             if id in StudentID:
                 print("Entrer marks:")
                 marks=math.floor(float(input()))
                 if marks<0 or marks >20:
                     print("Error")
                     print("Enter marks again")
                     marks=math.floor(float(input()))
                 if credits <=0:
                     print("Does not exit!!!")
                 else:
                     gpa= marks/credits
             else:
                 return 0
         else:
             return 0
         mark(cid,id,marks,gpa)
                  
#------------------------------------------Show--------------------------------------# 
class Start:
     def ShowCourses():
         print("Show lists of courses:\n")
         for i in range(0,len(Courses)):
             print("[",Course.describe(Courses[i]),"]",)


     def ShowStudent():
         print("Show lists of Student:\n")
         for i in range(0,len(Students)):
             print("[",Student.describe(Students[i]),"]",)

     def ShowMarks():
          print("Show marks of Student in courses:\n")
          for i in range(len(Students)):  
              print("[",mark.describe(Mark[i]),"]",)
              
     def descending():
         arr=np.array(MarkGPA)  
         arr[::-1].sort()
         print("The list after sorting is:\n",arr)

#-------------------------------------Main--------------------------------------#

     def StudentManagement():  
         print("*************************")
         print("""please select an option form list:
         1.  Input  Courses:
         2.  Stop """)
         option=int(input("YOU CHOOSE:"))
         if option==1:
             Nco=Course.input_number_courses()
             print("ADD COURSES:")
             for i in range( Nco):
                 Course.inputCourses()
                 Num=Student.input_number_student()
                 for i in range(Num):
                     print("INPUT  STUDENT:")
                     for i in range(Num):
                         Student.inputStudent()
                         Start.ShowCourses()
                         Start.ShowStudent()
                         print("1.ADD marks:")
                         mark.Mark_and_Gpa()
                         Start.ShowCourses()
                         Start.ShowStudent()
                         Start.ShowMarks()
                         break      
         else:
             print("Good bye:")
             exit()
         Start.descending()
            
             
if __name__ == '__main__':
    Start.StudentManagement()
    


