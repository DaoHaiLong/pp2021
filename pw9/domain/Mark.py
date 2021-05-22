import threading
Mark=[]
Mark_marks=[]
Mark_gpa=[]


class Marks():
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

    