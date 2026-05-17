from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QTextEdit, QLineEdit, QPushButton, QLabel, QFileDialog, QFrame
)
from PyQt6.QtCore import Qt, pyqtSignal

class VentanaPrincipal(QMainWindow):
    enviar_pregunta = pyqtSignal(str)
    solicitar_archivo = pyqtSignal()

    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self._configurar_ui()

    def _configurar_ui(self):
        self.setWindowTitle(f"ChatDoc - Sesión de {self.usuario}")
        self.resize(900, 700)
        self.setStyleSheet("background-color: #1e1e2e; color: #cdd6f4; font-family: 'Segoe UI';")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # Encabezado
        header = QFrame()
        header.setStyleSheet("background-color: #24273a; border-bottom: 1px solid #313244;")
        layout_h = QHBoxLayout(header)
        
        lbl_titulo = QLabel(f"📄 Analizando como: {self.usuario}")
        lbl_titulo.setStyleSheet("font-weight: bold; font-size: 14px; color: #89b4fa;")
        layout_h.addWidget(lbl_titulo)
        
        layout_h.addStretch()
        
        self.btn_archivo = QPushButton("📂 Cargar Archivo")
        self.btn_archivo.setStyleSheet("""
            QPushButton { background-color: #313244; padding: 8px 15px; border-radius: 5px; font-weight: bold; }
            QPushButton:hover { background-color: #45475a; }
        """)
        self.btn_archivo.clicked.connect(lambda: self.solicitar_archivo.emit())
        layout_h.addWidget(self.btn_archivo)
        
        layout.addWidget(header)

        # Área de Chat
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        self.chat_area.setStyleSheet("""
            background-color: #181825; 
            border: none; 
            padding: 20px; 
            font-size: 14px;
            line-height: 1.5;
        """)
        layout.addWidget(self.chat_area)

        # Barra de entrada
        input_frame = QFrame()
        input_layout = QHBoxLayout(input_frame)
        
        self.entrada_pregunta = QLineEdit()
        self.entrada_pregunta.setPlaceholderText("Escribe tu pregunta sobre el documento...")
        self.entrada_pregunta.setStyleSheet("""
            background-color: #313244; border: 1px solid #45475a; 
            border-radius: 10px; padding: 12px; color: #cdd6f4;
        """)
        self.entrada_pregunta.returnPressed.connect(self._manejar_envio)
        input_layout.addWidget(self.entrada_pregunta)

        self.btn_enviar = QPushButton("✈️")
        self.btn_enviar.setFixedSize(50, 42)
        self.btn_enviar.setStyleSheet("background-color: #89b4fa; border-radius: 10px; font-size: 18px;")
        self.btn_enviar.clicked.connect(self._manejar_envio)
        input_layout.addWidget(self.btn_enviar)

        layout.addWidget(input_frame)

    def _manejar_envio(self):
        texto = self.entrada_pregunta.text().strip()
        if texto:
            self.agregar_mensaje("Tú", texto, "#b4befe")
            self.entrada_pregunta.clear()
            self.enviar_pregunta.emit(texto)

    def agregar_mensaje(self, autor, mensaje, color):
        self.chat_area.append(f"<b style='color: {color}'>{autor}:</b> {mensaje}<br>")

    def seleccionar_archivo(self):
        file_filter = "Documentos (*.txt *.pdf *.json *.xml)"
        fname, _ = QFileDialog.getOpenFileName(self, 'Seleccionar archivo', '', file_filter)
        return fname