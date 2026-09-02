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
                if actual.exponente == exponente and actual.variable == variable:
                    # 1. Calcular el valor real con signo del término actual
                    val_actual = -actual.coeficiente if actual.signo == "-" else actual.coeficiente
                    
                    # 2. Calcular el valor real con signo del nuevo término
                    val_nuevo = -nuevo_polinomio.coeficiente if signo == "-" else nuevo_polinomio.coeficiente
                    
                    # 3. Sumar algebraicamente
                    total = val_actual + val_nuevo
                    
                    # 4. Actualizar el nodo existente con el nuevo signo y valor absoluto
                    actual.signo = "-" if total < 0 else "+"
                    actual.coeficiente = abs(total)
                    return
                anterior = actual
                actual = actual.siguiente
            anterior.siguiente = nuevo_polinomio
            nuevo_polinomio.siguiente = None


    def eliminar_termino(self, exponente):
        if self.cabeza is None:
            print("No existen terminos a eliminar")
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
            # Construimos cada término (ej: + 3 x^2)
            termino_str = f"{actual.signo} {actual.coeficiente}{actual.variable}^{actual.exponente}"
            elementos.append(termino_str)
            actual = actual.siguiente
            
        return " ".join(elementos)              




