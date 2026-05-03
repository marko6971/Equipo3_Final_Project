import sqlite3
import hashlib
import os

# Ruta a la base de datos en la carpeta raíz
RUTA_BD = os.path.join(os.path.dirname(__file__), "../../database/app_database.db")

def obtener_conexion():
    """Establece conexión con SQLite."""
    os.makedirs(os.path.dirname(RUTA_BD), exist_ok=True)
    conn = sqlite3.connect(RUTA_BD)
    conn.row_factory = sqlite3.Row
    return conn

def inicializar_bd():
    """Crea las tablas necesarias en español."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id           INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario      TEXT    NOT NULL UNIQUE,
            password_hash TEXT    NOT NULL,
            fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def _hashear_password(password: str) -> str:
    """Encripta la contraseña para seguridad."""
    return hashlib.sha256(password.encode()).hexdigest()

def registrar_usuario(usuario: str, password: str) -> tuple[bool, str]:
    """Registra un nuevo usuario en la BD."""
    if not usuario or not password:
        return False, "Usuario y contraseña son obligatorios."
    
    try:
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO usuarios (usuario, password_hash) VALUES (?, ?)",
            (usuario, _hashear_password(password))
        )
        conn.commit()
        conn.close()
        return True, "Registro exitoso."
    except sqlite3.IntegrityError:
        return False, f"El nombre de usuario '{usuario}' ya está en uso."

def validar_login(usuario: str, password: str) -> tuple[bool, str]:
    """Comprueba si las credenciales son correctas."""
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM usuarios WHERE usuario = ? AND password_hash = ?",
        (usuario, _hashear_password(password))
    )
    usuario_encontrado = cursor.fetchone()
    conn.close()

    if usuario_encontrado:
        return True, "Acceso correcto."
    return False, "Usuario o contraseña incorrectos."