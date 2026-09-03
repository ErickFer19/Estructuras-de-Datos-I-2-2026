class ControladorPolinomio:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        # Conectamos el botón de la Vista con la función del Controlador
        self.vista.configurar_comando_boton(self.manejar_agregar_termino)
        self.vista.configurar_comando_eliminar(self.manejar_eliminar_termino)

    def manejar_agregar_termino(self):
        datos = self.vista.obtener_datos()
        
        coef = datos["coeficiente"]
        exp = datos["exponente"]
        var = datos["variable"]
        signo = datos["signo"]
        
        if not coef or not exp:
            return 
        
        try:
            coef_num = float(coef) if '.' in coef else int(coef)
            exp_num = int(exp)
            
            self.modelo.agregar_termino(coef_num, exp_num, var, signo)
            polinomio_texto = self.modelo.obtener_representacion()
            
            self.vista.mostrar_polinomio(polinomio_texto)
            
        except ValueError:
            self.vista.mostrar_polinomio("Error: Coeficiente y Exponente deben ser numéricos.")

    def manejar_eliminar_termino(self):
        datos = self.vista.obtener_datos()

        exp = datos["exponente"]        

        if not exp:
            return

        try:
            exp_num = int(exp)
            self.modelo.eliminar_termino_por_exponente(exp_num)
            polinomio_texto = self.modelo.obtener_representacion()

            self.vista.mostrar_polinomio(polinomio_texto)
        except ValueError:
            self.vista.mostrar_polinomio("Error: No existe terminos con ese exponente")
