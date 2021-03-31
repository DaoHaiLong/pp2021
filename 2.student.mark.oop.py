# Student management
#------------------------------------list-----------------------------------#
Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Mark=[]

#-----------------------------------Student-----------------------------#

def input_number_student():
    Num=int(input("Enter the numbers of Student:"))
    if Num <=0:
        print("Does not exist!!!")
        return 0
    else:
        return Num


class  Student:
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
        Students.append(self)
        StudentID.append(self.id)
        
    def describe(self):
        print(["id:"],self.id, ["name:"],self.name, ["dob:"],self.dob)
    
def inputStudent():
    print("ADD STUDENT OF THIS COURSES:")
    print("Enter StudentID:")
    id=input()
    print("Enter StudentName:")
    name=input()
    print("Enter date of brith:")
    dob=input()
    Student(id,name,dob)        
        

#-----------------------------------------Course------------------------------#
def input_number_courses():
    Nco=int(input("Enter the numbers of course:"))
    if Nco<=0:
        print("Does not exist!!!")
        return 0
    else:
        return Nco

            
class Course:
    def __init__(self,cid,name):
        self.cid=cid
        self.name=name
        Courses.append(self)
        CoursesID.append(self.cid)
        
    def describe(self):
        print(["cid:"],self.cid , ["name:"],self.name)
    
def inputCourses():
    print("ADD COURSES:")
    print("Enter CoursesID:")
    cid=input()
    print("Enter CoursesName:")
    name=input()
    Course(cid,name)

#-------------------------------------------Mark------------------------------------#
class mark:
    def __init__(self,id,cid,marks):
        self.id=id
        self.cid=cid
        self.marks=marks
        Mark.append(self)
         
    def describe(self):
        print(["Coursesid:"],self.id, ["Studentid:"],self.cid, ["mark:"],self.marks)
    
def inputMark():
    print("Enter Courses id")
    cid=input()
    if cid in CoursesID:
        print("Enter Student ID:")
        id=input()
        if id in StudentID:
            print("Entrer marks:")
            marks=float(input())
        else:
            return 0      
    else:
        return 0
    mark(cid,id,marks)
        
#--------------------------------------Show--------------------------------#       

def ShowCourses():
    print("Show lists of courses:") 
    for i in range(0,len(Courses)):
        print("[",Course.describe(Courses[i]),"]",)   


def ShowStudent():
    print("Show lists of Student:")
    for i in range(0,len(Students)):
        print("[",Student.describe(Students[i]),"]",)  
        
def ShowMarks():
    print("Show marks of Student in courses:")
    for i in range(len(Students)):
        print("[",mark.describe(Mark[i]),"]",)
        
#-------------------------------------Main--------------------------------------#
        
def StudentManagement():
    print("*************************")
    print("""please select an option form list:
    1.  Input  Courses:
    2.  Stop """)
    option=int(input("YOU CHOOSE:"))
    if option==1:
        Nco=input_number_courses()
        print("1.ADD COURSES:")
        print("2.Stop")
        option1=int(input("YOU CHOOSE:"))
        if option1==1:       
            for i in range( Nco):
                inputCourses()
                Num=input_number_student()      
                for i in range(Num):                   
                    print("1. INPUT  STUDENT:")
                    print("2.Stop:")
                    option2=int(input("YOU CHOOSE:"))  
                    if option2==1:                     
                        for i in range(Num):
                            inputStudent()                  
                            ShowCourses()
                            ShowStudent()
                            print("1.ADD marks:")
                            print("2.Stop:")
                            option3=int(input("YOU CHOOSE:"))
                            if option3==1:
                                inputMark()
                                ShowCourses()
                                ShowStudent()                           
                                ShowMarks()
                                break
                            else:
                              exit()                         
                    else:
                       exit()
        else:
            exit()
    else:
        print("Good bye:")
        exit()
ShowMarks()        
StudentManagement()    


    
        
        
        
        
        