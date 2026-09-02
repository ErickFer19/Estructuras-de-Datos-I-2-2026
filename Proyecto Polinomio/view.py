import tkinter as tk

class VistaPolinomio(tk.Frame):
    """
    Clase que representa la Vista en el patrón MVC.
    Hereda de tk.Frame para integrarse en la ventana principal (root) provista por el main.py.
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(fill=tk.BOTH, expand=True)
        
        # Inicializar los componentes de la interfaz
        self._crear_widgets()

    def _crear_widgets(self):
        # Título principal
        self.label_titulo = tk.Label(self, text="Polinomio", font=("Arial", 16, "bold"))
        self.label_titulo.pack(pady=10)

        # Contenedor para las 4 entradas y sus etiquetas
        self.frame_inputs = tk.Frame(self)
        self.frame_inputs.pack(pady=10)

        # 1. Coeficiente
        f_coef = tk.Frame(self.frame_inputs)
        f_coef.pack(side=tk.LEFT, padx=5)
        self.entry_coef = tk.Entry(f_coef, width=8)
        self.entry_coef.pack()
        tk.Label(f_coef, text="coeficiente").pack()

        # 2. Exponente
        f_exp = tk.Frame(self.frame_inputs)
        f_exp.pack(side=tk.LEFT, padx=5)
        self.entry_exp = tk.Entry(f_exp, width=8)
        self.entry_exp.pack()
        tk.Label(f_exp, text="exponente").pack()

        # 3. Variable
        f_var = tk.Frame(self.frame_inputs)
        f_var.pack(side=tk.LEFT, padx=5)
        self.entry_var = tk.Entry(f_var, width=8)
        self.entry_var.pack()
        tk.Label(f_var, text="variable").pack()

        # 4. Signo
        f_signo = tk.Frame(self.frame_inputs)
        f_signo.pack(side=tk.LEFT, padx=5)
        self.entry_signo = tk.Entry(f_signo, width=8)
        self.entry_signo.pack()
        tk.Label(f_signo, text="signo").pack()

        # Botón central
        self.btn_accion = tk.Button(self, text="Button", width=12)
        self.btn_accion.pack(pady=10)

        # Área de visualización inferior (Caja de texto para mostrar polinomios)
        self.text_display = tk.Text(self, height=3, width=50, font=("Arial", 12))
        self.text_display.pack(pady=10)

    # --- Métodos de utilidad para que el Controlador interactúe con la Vista ---
    def obtener_datos(self):
        """Retorna un diccionario con los valores actuales de los campos de entrada."""
        return {
            "coeficiente": self.entry_coef.get(),
            "exponente": self.entry_exp.get(),
            "variable": self.entry_var.get(),
            "signo": self.entry_signo.get()
        }

    def mostrar_polinomio(self, texto):
        """Actualiza el cuadro de texto inferior con el polinomio formateado."""
        self.text_display.delete("1.0", tk.END)
        self.text_display.insert(tk.END, texto)

    def configurar_comando_boton(self, callback):
        """Permite al Controlador asignarle una función (evento) al botón."""
        self.btn_accion.config(command=callback)