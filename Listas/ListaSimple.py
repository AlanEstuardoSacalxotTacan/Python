class Nodo:
   def __init__(self, dato):
      self.dato = dato
      self.siguiente = None     
class ListaSimple:
    def __init__(self):
       self.Cabeza = None
       
    def InsertarAlFinal(self, dato):
        NuevoNodo = Nodo(dato)
        if not self.Cabeza:
            self.Cabeza=NuevoNodo
            return
        Actual=self.Cabeza
        while Actual.siguiente:
            Actual=Actual.siguiente
        Actual.siguiente=NuevoNodo
        
    def Eliminar(self, key):
        if not self.Cabeza:
            print("La lista está vacía")
            return
        if self.Cabeza.dato == key:
            self.Cabeza = self.Cabeza.siguiente
            return
        actual = self.Cabeza
        anterior = None
        while actual and actual.dato != key:
            anterior = actual
            actual = actual.siguiente
        if not actual:
            print(f"Elemento {key} no encontrado en la lista.")
            return
        anterior.siguiente = actual.siguiente
         
    def Mostrar(self):
        Actual=self.Cabeza
        while Actual:
            print(Actual.dato, end='->')
            Actual=Actual.siguiente
        print("None")
        
#prueba
Lista = ListaSimple()
Lista.InsertarAlFinal(1)
Lista.InsertarAlFinal(2)
Lista.InsertarAlFinal(3)
Lista.Mostrar()
Lista.Eliminar(2)
Lista.Mostrar()
print("Fin")    