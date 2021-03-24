# Student management
Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Mark=[]

def input_number_student():
    Num=int(input("Enter the numbers of Student:"))
    if Num <=0:
        print("Does not exist!!!")
        return 0
    else:
        return Num


def addStudent():
     print("ADD STUDENT OF THIS COURSES:") 
     info ={
         'ID': '',
         'Name':'',
         'DOB': ''
     }
     print("Enter StudentID:")
     info['ID']=id=input()
     print("Enter StudentName:")
     info['Name']=input()
     print("Enter date of brith:")
     info['DOB']=input()
     Students.append(info)
     StudentID.append(id)
    
 
def input_number_courses():
    Nco=int(input("Enter the numbers of course:"))
    if Nco<=0:
        print("Does not exist!!!")
        return 0
    else:
        return Nco
        

def addCourses():
    print("ADD COURSES:")
    infoC={
        'cID':'',
        'Name': ''
    }
    print("Enter CoursesID:")
    infoC['cID']=cid=input()
    print("Enter CoursesName:")
    infoC['Name']=input()
    Courses.append(infoC)
    CoursesID.append(cid)
    
def mark():
    print("Enter mark:")
    infoM={
        'cID':'',
        'ID':'',
        'marks':''
    }
    print("Enter Courses id")
    infoM['cID']=a=input()
    if a in CoursesID:
        print("Enter Student ID:")
        infoM['ID']=a1=input()
        if a1 in StudentID:
            print("Entrer marks:")
            infoM['marks']=float(input())
        else:
            return -1       
    else:
        return -1
        
        
    Mark.append(infoM)


def ShowCourses():
    print("Show lists of courses:") 
    for i in range(0,len(Courses)):
        print("[",Courses[i]['cID'],"]","[",Courses[i]['Name'],"]",)   


def ShowStudent():
    print("Show lists of Student:")
    for i in range(0,len(Students)):
        print("[",Students[i]['ID'],"]","[",Students[i]['Name'],"]","[",Students[i]['DOB'],"]",)  


def ShowMarks():
    print("Show marks of Student in courses:")
    for i in range(len(Students)):
        print("[",Mark[i]['cID'],"]","[",Mark[i]['ID'],"]","[",Mark[i]['marks'],"]",) 


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
                addCourses()
                Num=input_number_student()      
                for i in range(Num):                   
                    print("1. INPUT  STUDENT:")
                    print("2.Stop:")
                    option2=int(input("YOU CHOOSE:"))  
                    if option2==1:                     
                        for i in range(Num):
                            addStudent()                   
                            ShowCourses()
                            ShowStudent()
                            print("1.ADD marks:")
                            print("2.Stop:")
                            option3=int(input("YOU CHOOSE:"))
                            if option3==1:
                                mark()
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
