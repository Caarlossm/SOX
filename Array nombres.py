arr = ["macia", "juan", "jose", "ernesto"]
var_a_encontrar = "juan"

def busqueda_index(arr, elemento):
    try:
        return arr.index(elemento)
    except ValueError:
        return -1


indice = busqueda_index(arr, var_a_encontrar)
print(f"Usando index, el elemento {var_a_encontrar} se encuentra en el índice {indice}.")

print("Recorrido:")
for elemento in arr:
    print(elemento)

