class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListaCircular:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head  # type: ignore
        else:
            new_node = Node(data)
            current = self.head
            while current.next != self.head:  # type: ignore
                current = current.next  # type: ignore
            current.next = new_node  # type: ignore
            new_node.next = self.head  # type: ignore

    def imprimir(self):
        if not self.head:
            print("Lista vacía")
            return

        nodes = []
        current = self.head
        while True:
            nodes.append(str(current.data))  # type: ignore
            current = current.next  # type: ignore
            if current == self.head:
                break
        print(" -> ".join(nodes))

    def delete(self, key):
        if not self.head:
            return

        current = self.head

        # Caso especial: eliminar la cabeza
        if current.data == key:
            if current.next == self.head:
                # Solo un nodo
                self.head = None
            else:
                while current.next != self.head:  # type: ignore
                    current = current.next  # Ir al último nodo # type: ignore
                current.next = self.head.next  # type: ignore
                self.head = self.head.next
            return

        # Caso general
        prev = self.head
        current = self.head.next
        while current != self.head:
            if current.data == key:  # type: ignore
                prev.next = current.next  # type: ignore
                return
            prev = current
            current = current.next  # type: ignore


# Crear una lista circular y agregar elementos
cllist = ListaCircular()
cllist.append(100)
cllist.append(False)
cllist.append(3.12)
cllist.append("A")
cllist.append("Fernando jose Paz")
cllist.append("Comillas simples")

# Mostrar la lista
cllist.imprimir()

# Eliminar un elemento de la lista
cllist.delete(1)

# Mostrar la lista después de eliminar un elemento
cllist.imprimir()
