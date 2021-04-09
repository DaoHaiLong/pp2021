
Students=[]
StudentID=[]
Courses=[]
CoursesID=[]
Courses_credit=[]
Mark=[]
Mark_marks=[]
Mark_gpa=[]

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