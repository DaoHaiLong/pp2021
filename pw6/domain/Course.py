

Courses=[]
CoursesID=[]
Courses_credit=[]
CoursesName=[]

class Course:
    def __init__(self,cid,name,credit):
        self.cid=cid
        self.name=name
        self.credit=credit
        Courses.append(self)
        CoursesID.append(self.cid)
        Courses_credit.append(self.credit)
        CoursesName.append(self.name)
        
    def get_cid(self):
        return self.cid
    def get_name(self):
        return self.name
    def get_credit(self):
        return self.credit