class Pila:
    def __init__(self):
        self.items = []

    def es_vacia(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.es_vacia():
            return self.items.pop()
        else:
            return "La pila está vacía"

    def peek(self):
        if not self.es_vacia():
            return self.items[-1]
        else:
            return "La pila está vacía"

    def size(self):
        return len(self.items)

    def display(self):
        return self.items

# Crear una pila
mi_pila = Pila()

# Añadir elementos a la pila
mi_pila.push('a')
mi_pila.push('b')
mi_pila.push('c')
mi_pila.push(1)
mi_pila.push(2)
mi_pila.push(100)

# Mostrar la pila
print("Pila actual:", mi_pila.display())

# Ver el elemento superior de la pila
print("Cima de la pila:", mi_pila.peek())

# Eliminar elementos de la pila
print("Elemento eliminado:", mi_pila.pop())
print("Elemento eliminado:", mi_pila.pop())

# Mostrar el estado actual de la pila
print("Pila actual:", mi_pila.display())

# Mostrar el tamaño de la pila
print("Tamaño de la pila:", mi_pila.size())