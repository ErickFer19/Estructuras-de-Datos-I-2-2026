class Conjunto:
    def __init__(self, elementos = None):
        if elementos is None:
            self.elementos= []
        else:
            self.elementos = list(elementos)
            
    def agregar(self, elemento):
        if elemento not in self.elementos:
            self.elementos.append(elemento)
            
    def eliminar(self, elemento):
        if elemento in self.elementos:
            self.elementos.remove(elemento)
    
    def contiene(self, elemento):
        return elemento in self.elementos
    
    def union(self, otro_conjunto):
        nuevo_conjunto = Conjunto(self.elementos.copy())
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar(elemento)
        return nuevo_conjunto
    
    def interseccion(self, otro_conjunto):
        nuevo_conjunto = Conjunto()
        for elemento in self.elementos:
            if elemento in otro_conjunto.elementos:
                nuevo_conjunto.agregar(elemento)
        return nuevo_conjunto
    
    def diferencia(self, otro_conjunto):
        nuevo_conjunto = Conjunto()
        for elemento in self.elementos:
            if elemento not in otro_conjunto.elementos:
                nuevo_conjunto.agregar(elemento)
        return nuevo_conjunto
    
    def __str__(self):
        return "{" + ", ".join(str(e) for e in self.elementos) + "}"
    
    

conjunto1 = Conjunto([1, 2, 3])
conjunto2 = Conjunto([3, 4, 5])

print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)
union = conjunto1.union(conjunto2)
print("Unión:", union)
interseccion = conjunto1.interseccion(conjunto2)
print("Intersección:", interseccion)
diferencia = conjunto1.diferencia(conjunto2)
print("Diferencia (conjunto1 - conjunto2):", diferencia)
       
        