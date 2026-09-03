class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        
        
class Conjunto:
    def __init__(self, elementos):
        self.cabeza = None            
        
        
    def agregar_ultimo(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual_nodo = self.cabeza
            while actual_nodo.siguiente is not None:
                actual_nodo = actual_nodo.siguiente
                
            actual_nodo.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = None 
    
    def agregar_inicio(self, elemento):
        nuevo_nodo = Nodo(elemento)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            
    def agregar_lugar_cualquiera(self, elemento, posicion):
        nuevo_nodo = Nodo(elemento)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual_nodo = self.cabeza
            contador = 0
            while actual_nodo.siguiente is not None and contador < posicion - 1:
                actual_nodo = actual_nodo.siguiente
                contador += 1
            nuevo_nodo.siguiente = actual_nodo.siguiente
            actual_nodo.siguiente = nuevo_nodo    
            
    def eliminar(self, elemento):
        if self.cabeza is None:
            return
        if self.cabeza.valor == elemento:
            self.cabeza = self.cabeza.siguiente
            return
        actual_nodo = self.cabeza
        while actual_nodo.siguiente is not None:
            if actual_nodo.siguiente.valor == elemento:
                actual_nodo.siguiente = actual_nodo.siguiente.siguiente
                return
            actual_nodo = actual_nodo.siguiente 
            
    
    def contiene(self, elemento):
        actual_nodo = self.cabeza
        while actual_nodo is not None:
            if actual_nodo.valor == elemento:
                return True
            actual_nodo = actual_nodo.siguiente
        return False                  
    
    
    def Union(self, otro_conjunto):
        nuevo_conjunto = Conjunto()
        actual_nodo = self.cabeza
        while actual_nodo is not None:
            nuevo_conjunto.agregar_ultimo(actual_nodo.valor)
            actual_nodo = actual_nodo.siguiente
        actual_nodo = otro_conjunto.cabeza
        while actual_nodo is not None:
            if not nuevo_conjunto.contiene(actual_nodo.valor):
                nuevo_conjunto.agregar_ultimo(actual_nodo.valor)
            actual_nodo = actual_nodo.siguiente
        return nuevo_conjunto
    
    def Interseccion(self, otro_conjunto):
        nuevo_conjunto = Conjunto()
        actual_nodo = self.cabeza
        while actual_nodo is not None:
            if otro_conjunto.contiene(actual_nodo.valor):
                nuevo_conjunto.agregar_ultimo(actual_nodo.valor)
            actual_nodo = actual_nodo.siguiente
        return nuevo_conjunto        
        
    
    def Diferencia(self, otro_conjunto):
        nuevo_conjunto = Conjunto()
        actual_nodo = self.cabeza
        while actual_nodo is not None:
            if not otro_conjunto.contiene(actual_nodo.valor):
                nuevo_conjunto.agregar_ultimo(actual_nodo.valor)
            actual_nodo = actual_nodo.siguiente
        return nuevo_conjunto            
        