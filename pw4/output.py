
import numpy as np
import curses
from domain.Student import *
from domain.Course import *
from domain.Mark import *


py = curses.initscr() 
curses.start_color()

class outputs():
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
      
    displaycenteroutline("---Hello friend---")
    py.refresh()
    curses.napms(1000)
    displaycenteroutline("This is a Student management program ")
    py.refresh()
    curses.napms(2000)
    py.clear()
    py.refresh()
        
    
