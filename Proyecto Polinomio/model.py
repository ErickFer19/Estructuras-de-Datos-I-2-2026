class NodoPolinomio:
    def __init__(self, coeficiente, exponente, variable, signo):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.variable = variable
        self.signo = signo
        self.siguiente = None

class Polinomio:
    def __init__(self):
        self.cabeza = None


    def agregar_termino(self, coeficiente, exponente, variable, signo):
        nuevo_polinomio = NodoPolinomio(coeficiente, exponente, variable, signo)
        if self.cabeza is None:
            self.cabeza = nuevo_polinomio
        else:
            actual = self.cabeza
            anterior = None
            while actual is not None:
                if actual.exponente == exponente and actual.variable == variable or exponente == 0 and actual.exponente ==0:
                    val_actual = -actual.coeficiente if actual.signo == "-" else actual.coeficiente
                    val_nuevo = -nuevo_polinomio.coeficiente if signo == "-" else nuevo_polinomio.coeficiente
                    total = val_actual + val_nuevo
                    if total == 0:
                        if actual == self.cabeza:
                            self.cabeza = self.cabeza.siguiente
                            return
                        else:
                            anterior.siguiente = actual.siguiente
                            return
                    actual.signo = "-" if total < 0 else "+"
                    actual.coeficiente = abs(total)
                    return
                anterior = actual
                actual = actual.siguiente
            anterior.siguiente = nuevo_polinomio
            nuevo_polinomio.siguiente = None


    def eliminar_termino_por_exponente(self, exponente):
        if self.cabeza is None:
            return
        if self.cabeza.exponente == exponente:
            self.cabeza = self.cabeza.siguiente
            return
        anterior = None
        actual = self.cabeza
        while actual is not None:
            if actual.exponente == exponente:
                anterior.siguiente = actual.siguiente
                return
            else:
                anterior= actual
                actual = actual.siguiente

        print("No hay terminos con ese exponente")   
        
        

    def obtener_representacion(self):
        """Método nuevo para transformar la lista enlazada en un String para la Vista"""
        if self.cabeza is None:
            return "0"
        
        elementos = []
        actual = self.cabeza
        while actual is not None:
            if actual.exponente == 0:
                termino_str = f"{actual.signo} {actual.coeficiente}"
                elementos.append(termino_str)
            else:
                termino_str = f"{actual.signo} {actual.coeficiente}{actual.variable}^{actual.exponente}"
                elementos.append(termino_str)
            actual = actual.siguiente
            
        return " ".join(elementos)              





