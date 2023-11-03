
import threading
import multiprocessing
import time


def hilo_infinito():
    while True:
        print("Este es un hilo con un bucle infinito")
        time.sleep(1)

def proceso_infinito():
    while True:
        print("Este es un proceso con un bucle infinito")
        time.sleep(1)

if __name__ == "__main__":

    hilo = threading.Thread(target=hilo_infinito)
    

    proceso = multiprocessing.Process(target=proceso_infinito)
    
  
    hilo.start()
    proceso.start()
    proceso.join()
