import os
import subprocess
def main():
    print(" Current Working Directory:" , os.getcwd())
    # chamge directory at Home
    os.chdir(os.getenv("HOME"))
    cmd=""
    while True:
        cmd=input("DaoHaiLong@Acer:/> ")
        if cmd.split()[0] == "cd":
            try:
                #change directory from Home to the required folder
                os.chdir(cmd[3:]) 
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
