class NodoPolinomio:
    def __init__(self, coeficiente, exponente):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class Polinomio:
    def __init__(self):
        self.cabeza = None


    def agregar_termino(self, coeficiente, exponente):
        nuevo_polinomio = NodoPolinomio(coeficiente, exponente)
        if self.cabeza is None:
            self.cabeza = nuevo_polinomio
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_polinomio
            nuevo_polinomio.siguiente = None 


    def eliminar_termino(self, exponente):
        if self.cabeza is None:
            print("No existen terminos a eliminar")
        if self.cabeza.siguiente is None:
            if self.cabeza.exponente == exponente:
                self.cabeza = None
            else:
                print("No existen terminos con ese exponente")
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                if actual.siguiente.exponente == exponente:
                    actual.siguiente = actual.siguiente.siguiente
                else:
                    actual = actual.siguiente    




