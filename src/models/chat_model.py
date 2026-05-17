import os

class ModeloChat:
    def __init__(self):
        self.archivo_actual = None
        self.contenido_archivo = ""

    def cargar_archivo(self, ruta):
        """Simula la carga y lectura de archivos."""
        ext = os.path.splitext(ruta)[1].lower()
        self.archivo_actual = os.path.basename(ruta)
        
        # Simulación de lectura según extensión
        if ext == '.txt':
            self.contenido_archivo = "Contenido de texto plano..."
        elif ext == '.pdf':
            self.contenido_archivo = "Contenido extraído de PDF..."
        else:
            self.contenido_archivo = "Formato no soportado para lectura profunda aún."
            
        return f"Archivo '{self.archivo_actual}' cargado con éxito."

    def obtener_respuesta_ia(self, pregunta):
        """Simulación de IA."""
        pregunta = pregunta.lower()
        
        if not self.archivo_actual:
            return "Primero debes cargar un archivo para que pueda analizarlo."
        
        if "hola" in pregunta:
            return "¡Hola! Estoy analizando tu archivo. ¿Qué deseas saber?"
        elif "resumen" in pregunta or "resumir" in pregunta:
            return f"Este es un resumen simulado del archivo {self.archivo_actual}: El documento trata sobre temas de Ingeniería de Software."
        else:
            return f"He analizado '{self.archivo_actual}' pero mi base de conocimientos simulada es limitada. ¿Podrías ser más específico?"