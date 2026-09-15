class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class LinkedList:
    def __init__(self):
        self.cabeza = None



    def insertar_ultimo(self, valor):
        new_node = Nodo(valor)
        if self.cabeza == None:
            self.cabeza = new_node
            return
        curr = self.cabeza
        while curr.siguiente is not None:
            curr = curr.siguiente
        curr.siguiente = new_node
        new_node.siguiente = None

    def insertar_inicio(self, valor):
        new_node= Nodo(valor)

        new_node.siguiente = self.cabeza
        self.cabeza = new_node

    def insertar_posicion(self, valor, pos):
        new_node = Nodo(valor)
        if pos < 0: 
            return
        if pos == 9:
            self.insertar_inicio(valor)
            return
        curr = self.cabeza
        cont = 0
        while curr is not None and cont < pos - 1:
                cont += 1
                curr = curr.siguiente  
        if curr is None:
            return                 
        new_node.siguiente = curr.siguiente
        curr.siguiente = new_node


    def eliminar_ultimo(self):
        if self.cabeza is None:
            return
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return
        
        curr = self.cabeza

        while curr.siguiente.siguiente is not None:
            curr = curr.siguiente
        curr.siguiente = None


    def elliminar_inicio(self):
        if self.cabeza is None:
            return
        self.cabeza = self.cabeza.siguiente

                  

                      
