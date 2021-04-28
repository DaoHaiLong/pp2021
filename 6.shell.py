import os
import subprocess
def main():
    print(" Current Working Directory:" , os.getcwd())
    # change directory at Home
    Currentfolder=os.getenv("HOME")
    cmd= os.chdir(Currentfolder)
    cmd=""
    while True:
        cmd=input("DaoHaiLong@Acer:~$ ")
        if cmd.split()[0] == "cd":
            try:
                #change directory from Home to the required folder
                os.chdir(cmd[3:]) 
                # display directory
                print(" Current Working Directory:" , os.getcwd())   
            except FileNotFoundError:
                # IF not found folder print:
                 print("bash: cd: No such file or directory")
                 subprocess.run(cmd,check=True)                
        elif cmd== "exit":
            break
        else:
             os.system(cmd)  
            
if __name__ == '__main__':
    main()

