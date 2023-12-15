import os
from threading import Thread

def fun1():
    pid = os.getpid()
   
    print(f"El PID del proceso actual es: {pid}")


if __name__ == "__main__": 
    
    thread = Thread(target = fun1)

    thread.start()
    thread.join()

  

