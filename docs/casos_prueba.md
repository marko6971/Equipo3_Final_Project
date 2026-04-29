# Casos de Prueba — Sistema de Chat con IA para Consulta de Archivos

**Versión:** 1.0  
**Fecha:** 28/04/2026  
**Autor:** Jorge Edwin Guevara Ayala  
**Estándar de referencia:** IEEE 829  

---

## Índice

| ID | Nombre | Requerimiento | Tipo | Prioridad |
|---|---|---|---|---|
| CP-01 | Inicio de sesión con credenciales válidas | RF-01 | Funcional | Alta |
| CP-02 | Inicio de sesión con credenciales inválidas | RF-01 | Funcional | Alta |
| CP-03 | Carga de archivo TXT válido | RF-02 | Funcional | Alta |
| CP-04 | Carga de archivo PDF válido | RF-02 | Funcional | Alta |
| CP-05 | Carga de archivo con formato no soportado | RF-02 | Funcional | Alta |
| CP-06 | Envío de pregunta con archivo cargado | RF-03 | Integración | Alta |
| CP-07 | Envío de pregunta sin archivo cargado | RF-03 | Funcional | Alta |
| CP-08 | Guardado de conversación en SQLite | RF-04 | Integración | Alta |
| CP-09 | Persistencia de documento en MongoDB | RF-04 | Integración | Alta |
| CP-10 | Consulta del historial de conversaciones | RF-05 | Funcional | Media |
| CP-11 | Exportación de conversación a JSON | RF-06 | Funcional | Media |
| CP-12 | Exportación de conversación a XML | RF-07 | Funcional | Media |
| CP-13 | Cierre de sesión | RF-08 | Funcional | Alta |
| CP-14 | Tiempo de respuesta de la IA | RNF-01 | Rendimiento | Alta |
| CP-15 | Verificación de hash de contraseñas | RNF-02 | Seguridad | Alta |
| CP-16 | Usabilidad — flujo sin asistencia | RNF-03 | Usabilidad | Alta |
| CP-17 | Portabilidad — ejecución multiplataforma | RNF-04 | Portabilidad | Media |
| CP-18 | Mantenibilidad — estándar PEP 8 | RNF-05 | Mantenibilidad | Media |

---

## Pruebas Funcionales

---

### CP-01 — Inicio de sesión con credenciales válidas

| Campo | Detalle |
|---|---|
| **ID** | CP-01 |
| **Requerimiento** | RF-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | El usuario `admin` existe en la base de datos con contraseña `1234`. |
| **Datos de entrada** | Usuario: `admin` / Contraseña: `1234` |
| **Pasos** | 1. Abrir la aplicación. <br> 2. Ingresar usuario: `admin`. <br> 3. Ingresar contraseña: `1234`. <br> 4. Hacer clic en **Iniciar sesión**. |
| **Resultado esperado** | El sistema muestra la pantalla principal con el nombre del usuario en la barra superior. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-02 — Inicio de sesión con credenciales inválidas

| Campo | Detalle |
|---|---|
| **ID** | CP-02 |
| **Requerimiento** | RF-01 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | El usuario `admin` existe en la base de datos. |
| **Datos de entrada** | Usuario: `admin` / Contraseña: `xxxx` |
| **Pasos** | 1. Abrir la aplicación. <br> 2. Ingresar usuario: `admin`. <br> 3. Ingresar contraseña incorrecta: `xxxx`. <br> 4. Hacer clic en **Iniciar sesión**. |
| **Resultado esperado** | El sistema muestra el mensaje: _"Credenciales incorrectas"_. No concede acceso. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-03 — Carga de archivo TXT válido

| Campo | Detalle |
|---|---|
| **ID** | CP-03 |
| **Requerimiento** | RF-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | Usuario autenticado. Existe el archivo `prueba.txt` con contenido de texto. |
| **Datos de entrada** | Archivo: `prueba.txt` |
| **Pasos** | 1. Hacer clic en **Cargar archivo**. <br> 2. Seleccionar `prueba.txt`. <br> 3. Confirmar selección. |
| **Resultado esperado** | El sistema muestra el nombre del archivo activo y habilita el campo de preguntas. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-04 — Carga de archivo PDF válido

| Campo | Detalle |
|---|---|
| **ID** | CP-04 |
| **Requerimiento** | RF-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | Usuario autenticado. Existe el archivo `prueba.pdf` con contenido legible. |
| **Datos de entrada** | Archivo: `prueba.pdf` |
| **Pasos** | 1. Hacer clic en **Cargar archivo**. <br> 2. Seleccionar `prueba.pdf`. <br> 3. Confirmar selección. |
| **Resultado esperado** | El sistema extrae el texto del PDF, muestra el nombre del archivo activo y habilita el campo de preguntas. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-05 — Carga de archivo con formato no soportado

| Campo | Detalle |
|---|---|
| **ID** | CP-05 |
| **Requerimiento** | RF-02 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | Usuario autenticado. |
| **Datos de entrada** | Archivo: `datos.xlsx` |
| **Pasos** | 1. Hacer clic en **Cargar archivo**. <br> 2. Seleccionar un archivo `.xlsx`. <br> 3. Confirmar selección. |
| **Resultado esperado** | El sistema muestra el mensaje: _"Formato no soportado. Use TXT, PDF, JSON o XML."_ No carga el archivo. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-06 — Envío de pregunta con archivo cargado

| Campo | Detalle |
|---|---|
| **ID** | CP-06 |
| **Requerimiento** | RF-03 |
| **Tipo** | Integración |
| **Prioridad** | Alta |
| **Precondición** | Usuario autenticado con archivo TXT cargado. Conexión a internet activa. |
| **Datos de entrada** | Pregunta: _"¿De qué trata el documento?"_ |
| **Pasos** | 1. Escribir una pregunta en el campo de texto. <br> 2. Presionar **Enviar**. |
| **Resultado esperado** | El sistema muestra la respuesta generada por la IA en el área del chat en menos de 5 segundos. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-07 — Envío de pregunta sin archivo cargado

| Campo | Detalle |
|---|---|
| **ID** | CP-07 |
| **Requerimiento** | RF-03 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | Usuario autenticado. Sin archivo cargado. |
| **Datos de entrada** | Pregunta: _"¿Qué dice el documento?"_ |
| **Pasos** | 1. Escribir una pregunta sin haber cargado archivo. <br> 2. Presionar **Enviar**. |
| **Resultado esperado** | El sistema muestra el aviso: _"Debe cargar un archivo antes de hacer preguntas."_ |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-08 — Guardado de conversación en SQLite

| Campo | Detalle |
|---|---|
| **ID** | CP-08 |
| **Requerimiento** | RF-04 |
| **Tipo** | Integración |
| **Prioridad** | Alta |
| **Precondición** | El usuario realizó al menos una pregunta con respuesta. |
| **Datos de entrada** | Conversación activa con 1 pregunta y 1 respuesta. |
| **Pasos** | 1. Enviar una pregunta y recibir respuesta. <br> 2. Cerrar la aplicación. <br> 3. Reabrir la aplicación. <br> 4. Consultar el historial. |
| **Resultado esperado** | La conversación aparece en el historial con fecha, pregunta y respuesta correctas. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-09 — Persistencia de documento en MongoDB

| Campo | Detalle |
|---|---|
| **ID** | CP-09 |
| **Requerimiento** | RF-04 |
| **Tipo** | Integración |
| **Prioridad** | Alta |
| **Precondición** | MongoDB activo. Usuario autenticado. |
| **Datos de entrada** | Archivo: `prueba.pdf` |
| **Pasos** | 1. Cargar un archivo PDF. <br> 2. Verificar en MongoDB Compass la colección `archivos`. <br> 3. Confirmar que existe un documento con el contenido extraído. |
| **Resultado esperado** | Existe un documento en MongoDB con los campos: `nombre`, `tipo`, `contenido`, `id_conversacion`. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-10 — Consulta del historial de conversaciones

| Campo | Detalle |
|---|---|
| **ID** | CP-10 |
| **Requerimiento** | RF-05 |
| **Tipo** | Funcional |
| **Prioridad** | Media |
| **Precondición** | El usuario tiene al menos 2 conversaciones guardadas en SQLite. |
| **Datos de entrada** | Usuario con historial existente. |
| **Pasos** | 1. Hacer clic en **Historial**. <br> 2. Seleccionar una conversación de la lista. |
| **Resultado esperado** | El sistema muestra los mensajes de la conversación seleccionada con fecha y archivo asociado. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-11 — Exportación de conversación a JSON

| Campo | Detalle |
|---|---|
| **ID** | CP-11 |
| **Requerimiento** | RF-06 |
| **Tipo** | Funcional |
| **Prioridad** | Media |
| **Precondición** | Existe una conversación con al menos 2 mensajes. |
| **Datos de entrada** | Conversación activa. Formato seleccionado: JSON. |
| **Pasos** | 1. Seleccionar **Exportar**. <br> 2. Elegir formato **JSON**. <br> 3. Seleccionar ruta de guardado. <br> 4. Confirmar. |
| **Resultado esperado** | Se genera un archivo `.json` con estructura válida: `usuario`, `fecha`, `mensajes` (pregunta/respuesta). |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-12 — Exportación de conversación a XML

| Campo | Detalle |
|---|---|
| **ID** | CP-12 |
| **Requerimiento** | RF-07 |
| **Tipo** | Funcional |
| **Prioridad** | Media |
| **Precondición** | Existe una conversación con al menos 2 mensajes. |
| **Datos de entrada** | Conversación activa. Formato seleccionado: XML. |
| **Pasos** | 1. Seleccionar **Exportar**. <br> 2. Elegir formato **XML**. <br> 3. Seleccionar ruta de guardado. <br> 4. Confirmar. |
| **Resultado esperado** | Se genera un archivo `.xml` con estructura jerárquica válida y bien formada. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-13 — Cierre de sesión

| Campo | Detalle |
|---|---|
| **ID** | CP-13 |
| **Requerimiento** | RF-08 |
| **Tipo** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | El usuario tiene una sesión activa. |
| **Datos de entrada** | Sesión activa del usuario `admin`. |
| **Pasos** | 1. Hacer clic en **Cerrar sesión**. <br> 2. Confirmar en el diálogo de confirmación. |
| **Resultado esperado** | El sistema regresa a la pantalla de login. Los datos de sesión son eliminados de memoria. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

## Pruebas No Funcionales

---

### CP-14 — Tiempo de respuesta de la IA

| Campo | Detalle |
|---|---|
| **ID** | CP-14 |
| **Requerimiento** | RNF-01 |
| **Tipo** | Rendimiento |
| **Prioridad** | Alta |
| **Precondición** | Archivo TXT cargado. Conexión a internet activa. |
| **Datos de entrada** | Pregunta estándar de 10 palabras. |
| **Pasos** | 1. Registrar tiempo `t1` antes de enviar la pregunta. <br> 2. Enviar la pregunta. <br> 3. Registrar tiempo `t2` al recibir la respuesta. <br> 4. Calcular `t2 - t1`. |
| **Resultado esperado** | El tiempo total `t2 - t1` es **menor a 5 segundos**. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-15 — Verificación de hash de contraseñas

| Campo | Detalle |
|---|---|
| **ID** | CP-15 |
| **Requerimiento** | RNF-02 |
| **Tipo** | Seguridad |
| **Prioridad** | Alta |
| **Precondición** | El usuario `admin` está registrado en la base de datos. |
| **Datos de entrada** | Inspección directa de la tabla `usuarios` en SQLite. |
| **Pasos** | 1. Abrir la base de datos con **DB Browser for SQLite**. <br> 2. Consultar la tabla `usuarios`. <br> 3. Revisar el campo `contrasena`. |
| **Resultado esperado** | El campo muestra una cadena de **64 caracteres hexadecimales** (hash SHA-256), no texto plano. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-16 — Usabilidad — flujo sin asistencia

| Campo | Detalle |
|---|---|
| **ID** | CP-16 |
| **Requerimiento** | RNF-03 |
| **Tipo** | Usabilidad |
| **Prioridad** | Alta |
| **Precondición** | 2 usuarios externos que no conocen el sistema. |
| **Datos de entrada** | Usuario externo sin instrucciones previas. |
| **Pasos** | 1. Entregar la aplicación al usuario externo. <br> 2. Pedirle que cargue un archivo y haga una pregunta. <br> 3. Medir el tiempo hasta completar el flujo. |
| **Resultado esperado** | El usuario completa el flujo principal en **menos de 2 minutos** sin recibir ayuda. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-17 — Portabilidad — ejecución multiplataforma

| Campo | Detalle |
|---|---|
| **ID** | CP-17 |
| **Requerimiento** | RNF-04 |
| **Tipo** | Portabilidad |
| **Prioridad** | Media |
| **Precondición** | El proyecto está instalado en Windows 10 y Ubuntu 20.04. |
| **Datos de entrada** | Comando: `python main.py` en ambos sistemas. |
| **Pasos** | 1. Ejecutar `python main.py` en Windows. <br> 2. Verificar que la interfaz abre correctamente. <br> 3. Repetir en Ubuntu 20.04. |
| **Resultado esperado** | La aplicación abre y funciona correctamente en **ambos sistemas operativos** sin modificar el código. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

### CP-18 — Mantenibilidad — estándar PEP 8

| Campo | Detalle |
|---|---|
| **ID** | CP-18 |
| **Requerimiento** | RNF-05 |
| **Tipo** | Mantenibilidad |
| **Prioridad** | Media |
| **Precondición** | El código fuente está disponible en el repositorio. |
| **Datos de entrada** | Todos los archivos `.py` del proyecto. |
| **Pasos** | 1. Ejecutar `flake8 src/` en la terminal. <br> 2. Revisar el reporte de errores. |
| **Resultado esperado** | El reporte muestra **0 errores críticos** de estilo. Cada módulo tiene docstrings y comentarios. |
| **Resultado obtenido** | _(pendiente)_ |
| **Estado** | 🔲 Pendiente |

---

## Resumen de Estado

| Total de Casos | Ejecutados | Aprobados | Fallidos | Pendientes |
|---|---|---|---|---|
| 18 | 0 | 0 | 0 | 18 |

---

*Documento generado conforme al estándar IEEE 829.*
