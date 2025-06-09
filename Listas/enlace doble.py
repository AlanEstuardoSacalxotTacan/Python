#Problema2: Browser History 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  
        self.prev = None  

class HistorialNavegacion:
    def __init__(self):
        self.head = None
        self.tail = None  

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def Historial(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        print(" <-> ".join(nodes))

    def imprimir_web(self, key):
        current = self.head
        while current:
            if current.data == key:
                print(f"Dato encontrado: {current.data}")
                return
            current = current.next
        print("Dato no encontrado en la lista.")

histori=HistorialNavegacion()
histori.append("facebook.com")
histori.append("uedi.ingenieria.usac.edu.gt")
histori.append("intagram.com")
histori.append("youtube.com")

histori.Historial()


    