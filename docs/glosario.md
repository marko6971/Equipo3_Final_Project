# Glosario del Proyecto

**Proyecto:** Aplicación de Chat con IA sobre archivos  
**Versión:** 2.0  
**Fecha:** 28/04/2026  
**Equipo:** Equipo 3  

---

| Término | Definición |
|:---|:---|
| **API** | Interfaz de Programación de Aplicaciones. Conjunto de reglas que permite a dos sistemas comunicarse entre sí. |
| **API Key** | Código único de identificación que permite a la aplicación autenticarse y consumir servicios de inteligencia artificial externos. |
| **Arquitectura MVC** | Patrón de diseño Modelo-Vista-Controlador que separa los datos (Modelo), la interfaz (Vista) y la lógica de control (Controlador). |
| **bcrypt** | Algoritmo de hashing seguro utilizado para almacenar contraseñas de forma cifrada. |
| **Caso de Prueba (CP)** | Documento que describe las condiciones, pasos y resultados esperados para validar una funcionalidad específica del sistema. |
| **Caso de Uso (CU)** | Descripción de una secuencia de interacciones entre el usuario y el sistema para lograr un objetivo específico. |
| **Colección** | Equivalente a una tabla en MongoDB. Agrupa documentos con estructura similar. |
| **Conversación** | Conjunto de mensajes (preguntas y respuestas) intercambiados entre el usuario y el sistema bajo un contexto de archivo específico. |
| **CRLF / LF** | Caracteres de salto de línea. CRLF es el estándar en Windows; LF es el estándar en Linux/macOS. Git puede convertir entre ambos automáticamente. |
| **Docstring** | Cadena de texto dentro del código Python que documenta el propósito de una función, clase o módulo. |
| **Encoding** | Codificación de caracteres utilizada para representar texto. El proyecto usa UTF-8 como estándar. |
| **Exportación** | Proceso de generar un archivo externo (JSON o XML) con el contenido de una conversación almacenada. |
| **Fork** | Copia de un repositorio de GitHub en la cuenta de otro usuario, que permite trabajar de forma independiente y proponer cambios mediante Pull Requests. |
| **Hash** | Resultado de aplicar una función criptográfica a un dato (como una contraseña) para almacenarlo de forma segura sin revelar el valor original. |
| **Historial** | Registro de conversaciones previas almacenadas en la base de datos, accesible para consulta posterior. |
| **IA (Inteligencia Artificial)** | Modelo de lenguaje de gran tamaño (LLM) que procesa texto y genera respuestas coherentes basadas en un contexto dado. |
| **IEEE 829** | Estándar internacional para la documentación de planes y casos de prueba de software. |
| **IEEE 830** | Estándar internacional para la especificación de requisitos de software. |
| **JSON** | JavaScript Object Notation. Formato ligero de intercambio de datos estructurados en pares clave-valor. |
| **LLM** | Large Language Model. Modelo de inteligencia artificial entrenado con grandes volúmenes de texto para generar respuestas en lenguaje natural. |
| **MongoDB** | Sistema de gestión de bases de datos no relacional orientado a documentos. Almacena datos en formato BSON (similar a JSON). |
| **MVC** | Ver Arquitectura MVC. |
| **PDF** | Portable Document Format. Formato de archivo para documentos con diseño fijo. El sistema extrae su texto mediante `pdfplumber`. |
| **PEP 8** | Guía oficial de estilo para código Python que define convenciones de formato, nomenclatura y estructura. |
| **Persistencia** | Capacidad del sistema para guardar datos de manera que sobrevivan al cierre de la aplicación. |
| **pdfplumber** | Librería de Python utilizada para extraer texto e información de archivos PDF. |
| **Pull Request (PR)** | Solicitud para integrar cambios de una rama o fork hacia el repositorio principal en GitHub. |
| **PyInstaller** | Herramienta que empaqueta aplicaciones Python en ejecutables independientes (.exe para Windows). |
| **PyQt6** | Librería de Python para crear interfaces gráficas de escritorio basada en el framework Qt. |
| **python-dotenv** | Librería de Python que permite cargar variables de entorno desde un archivo `.env`. |
| **Requerimiento Funcional (RF)** | Descripción de una funcionalidad específica que el sistema debe realizar. |
| **Requerimiento No Funcional (RNF)** | Descripción de una característica de calidad del sistema (rendimiento, seguridad, usabilidad, etc.). |
| **RF** | Ver Requerimiento Funcional. |
| **RNF** | Ver Requerimiento No Funcional. |
| **SHA-256** | Algoritmo de hash criptográfico que genera una cadena de 64 caracteres hexadecimales. Usado para proteger contraseñas. |
| **Simulación de IA** | Módulo del sistema que genera respuestas predefinidas o basadas en búsqueda de palabras clave cuando no se dispone de una API de IA externa. |
| **SQLite** | Sistema de gestión de bases de datos relacional ligero, sin servidor, que almacena los datos en un archivo local. |
| **TDCU** | Tabla de Descripción de Caso de Uso. Formato estándar para detallar los pasos, actores y reglas de un requerimiento funcional. |
| **Tkinter** | Librería estándar de Python para crear interfaces gráficas de escritorio. |
| **Trazabilidad** | Capacidad de relacionar un requerimiento con su diseño, código y pruebas correspondientes. |
| **TXT** | Archivo de texto plano. Formato más simple soportado por el sistema. |
| **UTF-8** | Estándar de codificación de caracteres que soporta todos los idiomas. Usado en todos los archivos del proyecto. |
| **XML** | eXtensible Markup Language. Formato de texto estructurado mediante etiquetas jerárquicas, usado para exportar conversaciones. |
| **.env** | Archivo de configuración que almacena variables de entorno sensibles (como API Keys) fuera del código fuente. |
| **.gitignore** | Archivo de configuración de Git que especifica qué archivos o carpetas no deben ser rastreados por el control de versiones. |
| **.gitkeep** | Archivo vacío utilizado para que Git rastree carpetas vacías, ya que Git no versiona directorios sin contenido. |
