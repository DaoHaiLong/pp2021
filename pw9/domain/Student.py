
Students=[]
StudentID=[]
StudentName=[]
Studentdob=[]

class  Student():
    def __init__(self,id,name,dob):
        self.id=id
        self.name=name
        self.dob=dob
        Students.append(self) 
        StudentID.append(self.id)
        StudentName.append(self.name)
        Studentdob.append(self.dob)

    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob
    