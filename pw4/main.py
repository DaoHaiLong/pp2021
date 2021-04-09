
import curses
from output import outputs
from input import inputs
from domain.Student import *
from domain.Course import *
from domain.Mark import *


py = curses.initscr() 
curses.start_color()
class mains():
    def StudentManagement():    
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
                 Nco=inputs.input_number_course()
                 py.clear()
                 py.refresh()
                 for i in range( Nco):
                     py.addstr(f"Course { i+1}\n")
                     inputs.inputCourses()
                     py.refresh()
                     py.addstr("enter number of student: ")
                     Num=inputs.input_number_student()
                     py.clear()
                     py.refresh()
                     for i in range(Num):
                         py.addstr(f"INPUT  STUDENT {i +1}:\n")
                         inputs.inputstudent()
                         py.clear()
                         py.refresh()
                         inputs.inputmark()
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
                 inputs.Gpa()
             if option1==2:
                 outputs.ShowStudent()
             if option1==3:
                 outputs.ShowCourses()
             if option1==4:
                 outputs.ShowMarks()
             if option1==5:
                 outputs.GPA_decending()
             elif option1==6:
                py.addstr("  Good bye,see you again\n  ")
                py.refresh()
                curses.napms(1000)
                curses.endwin()
                exit()  
                                    

if __name__ == '__main__':
      
    mains.StudentManagement()
    