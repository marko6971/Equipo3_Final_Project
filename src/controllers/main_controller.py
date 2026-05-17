from views.main_window import VentanaPrincipal
from models.chat_model import ModeloChat

class ControladorPrincipal:
    def __init__(self, usuario):
        self.modelo = ModeloChat()
        self.vista = VentanaPrincipal(usuario)

        # Conectar señales
        self.vista.enviar_pregunta.connect(self._procesar_pregunta)
        self.vista.solicitar_archivo.connect(self._cargar_archivo)

    def mostrar(self):
        self.vista.show()

    def _cargar_archivo(self):
        ruta = self.vista.seleccionar_archivo()
        if ruta:
            mensaje = self.modelo.cargar_archivo(ruta)
            self.vista.agregar_mensaje("Sistema", mensaje, "#a6e3a1")

    def _procesar_pregunta(self, pregunta):
        respuesta = self.modelo.obtener_respuesta_ia(pregunta)
        self.vista.agregar_mensaje("AI Assistant", respuesta, "#fab387")