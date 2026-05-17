import sys
import os

# Agrega la carpeta src al path de python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from PyQt6.QtWidgets import QApplication
from controllers.login_controller import ControladorLogin

def iniciar_app():
    app = QApplication(sys.argv)

    # Instanciar y mostrar el controlador de login
    controlador = ControladorLogin()
    controlador.mostrar()

    sys.exit(app.exec())

if __name__ == "__main__":
    iniciar_app()