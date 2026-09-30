from flask import Flask
from controller.task_controller import register_routes

app = Flask(__name__)

# Registramos las rutas del controlador
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True, port=5000)