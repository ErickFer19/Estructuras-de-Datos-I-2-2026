class Node:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None


class LinkedDoubleList:
    def __init__(self):
        self.cabeza = None

    def insertar_ultimo(self, valor):
        new_node = Node(valor)
        if self.cabeza is None:
            self.cabeza = new_node
            return
        curr = self.cabeza
        while curr.siguiente is not None:
            curr = curr.siguiente

        curr.siguiente = new_node
        new_node.anterior = curr


    def insertar_inicio(self, valor):
        new_node = Node(valor)
        if self.cabeza is None:
            self.cabeza = new_node
            return
        new_node.siguiente = self.cabeza
        self.cabeza.anterior = new_node
        self.cabeza = new_node  


    def eliminar_ultimo(self):
        if self.cabeza is None:
            return
        if self.cabeza.siguiente is None:
            self.cabeza = None

        curr = self.cabeza
        while curr.siguiente is not None:
            curr = curr.siguiente

        penultimo = curr.anterior
        penultimo.siguiente = None
        curr.anterior = None    

            

                
