if __name__ == "__main__":
    pila = []

    # Agregar elementos a la pila
    pila.append(1)
    pila.append(2)
    pila.append(3)

    print("Mi pila después de agregar elementos:", pila)

    # Eliminar el último elemento de la pila (pop)
    elemento_eliminado = pila.pop()
    print("Elemento eliminado de la pila:", elemento_eliminado)
    print("Mi pila después de eliminar un elemento:", pila)
