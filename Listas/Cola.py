class Cola:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Comprueba si la cola está vacía."""
        return len(self.items) == 0

    def encolar(self, item):
        """Añade un elemento al final de la cola."""
        self.items.append(item)

    def desencolar(self):
        """Elimina y devuelve el primer elemento de la cola.
        Si la cola está vacía, retorna None."""
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        """Devuelve el primer elemento de la cola sin eliminarlo.
        Si la cola está vacía, retorna None."""
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def size(self):
        """Devuelve el número de elementos en la cola."""
        return len(self.items)

    def display(self):
        """Muestra el contenido actual de la cola."""
        return self.items

# Ejemplo de uso
mi_cola = Cola()

# Añadir elementos a la cola
mi_cola.encolar('a')
mi_cola.encolar('b')
mi_cola.encolar('c')

# Mostrar el contenido de la cola
print("Cola actual:", mi_cola.display())

# Ver el primer elemento de la cola
print("Frente de la cola:", mi_cola.peek())

# Eliminar elementos de la cola
print("Elemento eliminado:", mi_cola.desencolar())
print("Elemento eliminado:", mi_cola.desencolar())

# Mostrar el estado actual de la cola
print("Cola actual:", mi_cola.display())

# Mostrar el tamaño de la cola
print("Tamaño de la cola:", mi_cola.size())