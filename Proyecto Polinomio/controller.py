class ControladorPolinomio:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        # Conectamos el botón de la Vista con la función del Controlador
        self.vista.configurar_comando_boton(self.manejar_agregar_termino)

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
            
            # Usamos el modelo pasado por parámetro
            self.modelo.agregar_termino(coef_num, exp_num, var, signo)
            polinomio_texto = self.modelo.obtener_representacion()
            
            self.vista.mostrar_polinomio(polinomio_texto)
            
        except ValueError:
            self.vista.mostrar_polinomio("Error: Coeficiente y Exponente deben ser numéricos.")