# Especificación Suplementaria

**Proyecto:** Aplicación de Chat con IA sobre archivos  
**Versión:** 2.0  
**Fecha:** 28/04/2026  
**Equipo:** Equipo 3  
**Estándar de referencia:** IEEE 830  

---

## 1. Introducción

Este documento define los requisitos de calidad, restricciones técnicas y estándares que el sistema de Chat con IA debe cumplir para garantizar su correcto funcionamiento, mantenibilidad y coherencia con la arquitectura definida por el equipo.

Complementa el Documento de Requerimientos (versión 2.0) y debe leerse en conjunto con los diagramas UML, el Plan de Pruebas y la Matriz de Trazabilidad del proyecto.

---

## 2. Restricciones de diseño e implementación

| Restricción | Detalle |
|---|---|
| **Lenguaje de programación** | Python 3.10 o superior. |
| **Interfaz gráfica** | Tkinter o PyQt6. No se permite desarrollo web ni móvil. |
| **Base de datos relacional** | SQLite para usuarios, sesiones, conversaciones e historial. |
| **Base de datos no relacional** | MongoDB para almacenamiento del contenido procesado de archivos. |
| **Patrón de arquitectura** | Modelo-Vista-Controlador (MVC). |
| **Entorno de ejecución** | Local. No requiere conexión a internet para funcionalidades básicas. |

---

## 3. Requisitos de interfaz externa

### 3.1 Servicios de inteligencia artificial
- Conexión opcional vía API REST a modelos como OpenAI, Groq o similares.
- Si no se cuenta con API, el sistema debe activar un módulo de simulación de respuestas.
- Las claves de API (API Keys) **no deben estar escritas directamente en el código**; deben leerse desde un archivo `.env` o variables de entorno del sistema.

### 3.2 Manejo de archivos
- **TXT:** Lectura directa con Python usando codificación UTF-8.
- **PDF:** Extracción de texto mediante la librería `pdfplumber`.
- **JSON:** Lectura y parseo con el módulo estándar `json`.
- **XML:** Lectura y parseo con `xml.etree.ElementTree`.

---

## 4. Atributos de calidad

### 4.1 Rendimiento
- El sistema debe responder en **menos de 5 segundos** en escenarios de simulación o consulta local.
- La carga de archivos no debe superar los **3 segundos** para archivos de hasta 5 MB.

### 4.2 Usabilidad
- La interfaz debe ser intuitiva para usuarios con conocimientos básicos de informática.
- El flujo principal (login → cargar archivo → preguntar → exportar) debe completarse sin necesidad de documentación adicional.

### 4.3 Seguridad
- Las contraseñas de usuario deben almacenarse con hash (SHA-256 o bcrypt). No se permite texto plano.
- Las claves de API deben gestionarse mediante variables de entorno o archivo `.env` excluido del repositorio.

### 4.4 Mantenibilidad
- El código debe seguir el estándar **PEP 8**.
- Cada módulo debe incluir **docstrings** descriptivos.
- La estructura del proyecto debe seguir el patrón MVC con separación clara de responsabilidades.

### 4.5 Portabilidad
- La aplicación debe ejecutarse en **Windows 10/11** y **Ubuntu 20.04 o superior** sin modificar el código fuente.
- Debe ser empaquetable como ejecutable `.exe` para Windows mediante `PyInstaller`.

### 4.6 Disponibilidad
- La aplicación debe funcionar en modo **offline** para las funcionalidades que no requieran IA externa (carga de archivos, historial, exportación).

---

## 5. Estándares aplicados

| Estándar | Aplicación |
|---|---|
| **IEEE 830** | Especificación de requisitos de software. |
| **IEEE 829** | Plan de pruebas y casos de prueba. |
| **PEP 8** | Estilo y formato del código Python. |
| **MVC** | Patrón de arquitectura del sistema. |
| **UTF-8** | Codificación de caracteres en todos los archivos del proyecto. |

---

## 6. Restricciones adicionales

- El uso de Python es **obligatorio**.
- El uso de base de datos es **obligatorio** (al menos SQLite).
- MongoDB es parte de la arquitectura definida; su implementación puede ser gradual.
- El tiempo de desarrollo está limitado al calendario académico del semestre.
- No se permite el uso de frameworks web (Django, Flask, FastAPI) para la interfaz de usuario.

---

## 7. Supuestos técnicos

- El equipo de desarrollo tiene acceso a Python 3.10+ y puede instalar las dependencias necesarias.
- Los archivos de prueba estarán disponibles en formatos válidos (TXT, PDF, JSON, XML legibles).
- MongoDB puede instalarse localmente o usarse mediante MongoDB Atlas en su capa gratuita.
- El entorno de desarrollo es Windows; las pruebas de portabilidad se realizarán en Ubuntu.

---

## 8. Dependencias del proyecto

```
pdfplumber>=0.9.0
pymongo>=4.0.0
python-dotenv>=1.0.0
PyQt6>=6.4.0
bcrypt>=4.0.0
```

> Nota: Tkinter está incluido en la instalación estándar de Python y no requiere instalación adicional.

---

## 9. Observaciones finales

Este documento es complementario al Documento de Requerimientos versión 2.0. Cualquier cambio en la arquitectura o tecnologías debe reflejarse en ambos documentos para mantener la coherencia del proyecto.
