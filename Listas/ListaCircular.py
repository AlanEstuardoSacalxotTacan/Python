class Node:
    # Clase que representa un nodo en la lista circular
    def __init__(self, data):
        self.data = data  # Dato almacenado en el nodo
        self.next = None  # Puntero al siguiente nodo

class ListaCircular:
    # Clase que representa una lista enlazada circular
    def __init__(self):
        self.head = None  # Inicialmente, la lista está vacía

    def append(self, data):
        # Método para agregar un nuevo nodo a la lista
        if not self.head:
            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
            self.head = Node(data)
            self.head.next = self.head  # Apunta a sí mismo para hacerla circular
        else:
            # Si la lista no está vacía, recorrer hasta el último nodo
            new_node = Node(data)
            current = self.head
            while current.next != self.head:
                current = current.next
            # Insertar el nuevo nodo al final y hacer que apunte a la cabeza
            current.next = new_node
            new_node.next = self.head

    def imprimir(self):
        # Método para imprimir la lista en formato legible
        nodes = []
        current = self.head
        if self.head:
            while True:
                nodes.append(str(current.data))  # Agregar el dato del nodo a la lista
                current = current.next
                if current == self.head:
                    break  # Detenerse cuando se completa un ciclo en la lista
        print(" -> ".join(nodes))

    def delete(self, key):
        # Método para eliminar un nodo con un valor específico
        if self.head.data == key:
            # Si el nodo a eliminar es la cabeza
            current = self.head
            while current.next != self.head:
                current = current.next  # Buscar el último nodo
            if self.head == self.head.next:
                # Si solo hay un nodo en la lista
                self.head = None
            else:
                # Si hay más de un nodo, reasignar la cabeza y actualizar enlaces
                current.next = self.head.next
                self.head = self.head.next
        else:
            # Si el nodo a eliminar no es la cabeza
            current = self.head
            prev = None
            while current.next != self.head:
                prev = current
                current = current.next
                if current.data == key:
                    # Reasignar los enlaces para eliminar el nodo
                    prev.next = current.next
                    break

# Crear una lista circular y agregar elementos
cllist = ListaCircular()
cllist.append(100)
cllist.append(False)
cllist.append(3.12)
cllist.append('A')
cllist.append('Fernando jose Paz')
cllist.append('Comillas simples')

# Mostrar la lista
cllist.imprimir()

# Eliminar un elemento de la lista
cllist.delete(1)

# Mostrar la lista después de eliminar un elemento
cllist.imprimir()