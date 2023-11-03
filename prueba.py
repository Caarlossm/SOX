
def metodo1():

    print ("Hola")

def metodo2():
    a = "Que tal?" 
    print(a)
    a = 6 / 2
    print(a)

def metodo3(): 

    a = 2
    b = 5
    print (a + b) 


def resta(numero1,numero2):
    c = numero1 - numero2
    return c

def multiplicar(numero1,numero2):
    d = numero1 * numero2
    return d


def print_k(array):  
    for n in array:    
         print (n)


if __name__ == "__main__": 

    metodo1()
    metodo2()
    metodo3()
    c = resta(5,3)
    d = multiplicar(8,6)
    print (c)
    print (d)
    
    array = ["pepito","pedro","nacho"]
    print_k(array)

