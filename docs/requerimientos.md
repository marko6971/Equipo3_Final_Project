Documento de Levantamiento de Requerimientos
### 1. Información general
Proyecto: Aplicación de Chat con IA sobre archivos
Cliente: Profesor (Materia: Ingeniería de Software)
Equipo: Equipo 3
Fecha: [poner fecha]

Descripción:
Desarrollo de una aplicación de escritorio en Python que permita cargar archivos, realizar consultas sobre su contenido mediante IA (o simulación), almacenar conversaciones en base de datos y exportarlas en formato JSON y/o XML.

### 2. Objetivo del sistema
Desarrollar una aplicación tipo chat que permita al usuario interactuar con el contenido de archivos cargados, simulando o utilizando un modelo de inteligencia artificial, con persistencia de datos y exportación de conversaciones.

### 3. Alcance
Incluye:

Interfaz gráfica tipo chat
Sistema de login
Carga de archivos (TXT/PDF)
Consulta a IA o simulación
Almacenamiento en base de datos
Exportación JSON/XML
No incluye:

Entrenamiento de modelos de IA
Aplicación web o móvil
### 4. Stakeholders
Usuario final: Estudiante
Cliente: Profesor
Desarrolladores: Equipo 3
### 5. Requerimientos funcionales
RF1. Login

El sistema debe permitir acceso mediante usuario y contraseña.
RF2. Interfaz tipo chat

Mostrar conversación completa
Campo de entrada de texto
Botón de envío
Diferenciar mensajes (usuario / sistema)
RF3. Carga de archivos

Permitir seleccionar archivo desde el sistema
Mostrar nombre del archivo cargado
Soportar TXT y PDF
RF4. Consulta al sistema

Permitir al usuario hacer preguntas
Responder basado en el archivo cargado
Simular respuesta si no hay API
RF5. Persistencia

Guardar conversaciones en base de datos
Registrar:
ID
fecha/hora
mensajes
archivo asociado
RF6. Exportación

Exportar conversaciones a JSON y/o XML
### 6. Requerimientos no funcionales
RNF1: Aplicación en Python
RNF2: Interfaz gráfica amigable
RNF3: Uso de base de datos relacional
RNF4: Respuesta rápida (<2 segundos en simulación)
RNF5: Código estructurado y mantenible
### 7. Casos de uso principales
CU1: Iniciar sesión

Usuario ingresa credenciales
Sistema valida acceso
CU2: Cargar archivo

Usuario selecciona archivo
Sistema lo registra
CU3: Realizar consulta

Usuario escribe pregunta
Sistema responde
CU4: Guardar conversación

Sistema almacena automáticamente
CU5: Exportar conversación

Usuario selecciona formato
Sistema genera archivo JSON/XML
### 8. Restricciones
Uso de Python obligatorio
Uso de base de datos
API de IA opcional (puede simularse)
Tiempo limitado de desarrollo
### 9. Supuestos
El usuario tendrá conocimientos básicos de uso
Los archivos serán legibles (TXT/PDF válidos)
Se trabajará en entorno local
### 10. Riesgos
No encontrar API gratuita
Problemas al leer PDF
Falta de tiempo
Mitigación:

Simulación de IA
Uso de TXT como respaldo
Priorizar funcionalidades mínimas