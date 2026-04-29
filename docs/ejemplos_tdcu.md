# Documentación de Requerimientos y TDCU

**Sistema:** Sistema de Chat con IA para Consulta de Archivos  
**Versión:** 2.0  
**Fecha:** 28/04/2026  
**Autor:** Jorge Edwin Guevara Ayala  
**Equipo:** Equipo 3  

---

## Propósito

Este documento describe los requerimientos funcionales y no funcionales del sistema, así como sus Tablas de Descripción de Casos de Uso (TDCU), para apoyar la planeación, diseño, implementación y validación del proyecto conforme a prácticas de Ingeniería de Software.

---

## Alcance

El sistema permitirá a un usuario autenticarse, cargar archivos TXT, PDF, JSON o XML, realizar preguntas sobre su contenido mediante un chat asistido por IA o simulación, almacenar conversaciones en SQLite, persistir documentos procesados en MongoDB y exportar conversaciones a JSON y XML.

---

## 1. Requerimientos funcionales

### RF-01 — Iniciar Sesión

| Campo | Descripción |
|---|---|
| **ID** | RF-01 |
| **Nombre** | Iniciar Sesión |
| **Descripción** | El sistema permite al usuario autenticarse mediante nombre de usuario y contraseña para acceder a las funcionalidades del sistema. |
| **Actor(es)** | Usuario registrado |
| **Precondiciones** | El usuario debe estar registrado en el sistema. La base de datos SQLite debe estar disponible. |
| **Flujo principal** | 1. El usuario abre la aplicación. 2. El sistema muestra el formulario de inicio de sesión. 3. El usuario ingresa su nombre de usuario y contraseña. 4. El sistema valida las credenciales contra la base de datos. 5. El sistema concede acceso y muestra la pantalla principal. |
| **Flujos alternativos** | 4a. Si las credenciales son incorrectas, el sistema muestra un mensaje de error y permite reintentar. |
| **Postcondiciones** | El usuario queda autenticado y puede usar el sistema. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

---

### RF-02 — Interfaz tipo chat

| Campo | Descripción |
|---|---|
| **ID** | RF-02 |
| **Nombre** | Interfaz tipo chat |
| **Descripción** | El sistema debe mostrar una interfaz tipo chat que permita visualizar la conversación completa, ingresar preguntas, enviar mensajes y diferenciar visualmente los mensajes del usuario y del sistema. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | El usuario debe haber iniciado sesión. |
| **Flujo principal** | 1. El sistema muestra el área de chat vacía. 2. El usuario escribe un mensaje en el campo de texto. 3. El usuario presiona el botón Enviar o la tecla Enter. 4. El sistema muestra el mensaje del usuario alineado a la derecha. 5. El sistema muestra la respuesta alineada a la izquierda. |
| **Flujos alternativos** | 2a. Si el campo está vacío, el sistema no procesa la solicitud. |
| **Postcondiciones** | La conversación se muestra correctamente en la interfaz. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

---

### RF-03 — Carga de archivos

| Campo | Descripción |
|---|---|
| **ID** | RF-03 |
| **Nombre** | Carga de archivos |
| **Descripción** | El sistema permite al usuario cargar un archivo en formato TXT, PDF, JSON o XML para ser procesado y consultado mediante el chat. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | El usuario debe haber iniciado sesión. El archivo debe ser de tipo TXT, PDF, JSON o XML. |
| **Flujo principal** | 1. El usuario hace clic en "Cargar archivo". 2. El sistema abre el explorador de archivos. 3. El usuario selecciona un archivo compatible. 4. El sistema lee y procesa el contenido del archivo. 5. El sistema confirma la carga exitosa y muestra el nombre del archivo activo. |
| **Flujos alternativos** | 3a. Si el archivo no es de un formato soportado, el sistema muestra un mensaje de error. 4a. Si el archivo está vacío o corrupto, el sistema notifica al usuario. |
| **Postcondiciones** | El contenido del archivo queda disponible para ser consultado en el chat. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

---

### RF-04 — Consulta al sistema (IA o simulación)

| Campo | Descripción |
|---|---|
| **ID** | RF-04 |
| **Nombre** | Consulta al sistema |
| **Descripción** | El sistema permite al usuario escribir y enviar preguntas relacionadas con el contenido del archivo cargado, recibiendo una respuesta generada por el módulo de IA o por simulación. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | El usuario debe haber iniciado sesión y tener un archivo cargado. |
| **Flujo principal** | 1. El usuario escribe una pregunta en el campo de texto. 2. El usuario presiona "Enviar" o la tecla Enter. 3. El sistema envía la pregunta junto con el contenido del archivo al módulo de IA. 4. El módulo de IA o simulación genera una respuesta. 5. El sistema muestra la respuesta en el área del chat. |
| **Flujos alternativos** | 2a. Si el campo está vacío, el sistema no procesa la solicitud. 3a. Si no hay archivo cargado, el sistema muestra un aviso. 4a. Si el servicio de IA no responde, el sistema activa el módulo de simulación. |
| **Postcondiciones** | La pregunta y la respuesta quedan registradas en la conversación activa. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

---

### RF-05 — Persistencia de conversaciones en SQLite

| Campo | Descripción |
|---|---|
| **ID** | RF-05 |
| **Nombre** | Persistencia de conversaciones en SQLite |
| **Descripción** | El sistema almacena automáticamente cada conversación (preguntas y respuestas) en la base de datos SQLite, asociada al usuario y al archivo consultado. |
| **Actor(es)** | Sistema (automático) |
| **Precondiciones** | El usuario debe estar autenticado y haber enviado al menos un mensaje. |
| **Flujo principal** | 1. El usuario envía un mensaje. 2. El sistema recibe la respuesta de la IA o simulación. 3. El sistema guarda el par pregunta-respuesta en la tabla Mensaje. 4. El sistema asocia el mensaje a la conversación activa en la tabla Conversacion. |
| **Flujos alternativos** | 3a. Si la base de datos no está disponible, el sistema registra el error en un log y notifica al usuario. |
| **Postcondiciones** | El mensaje queda persistido en SQLite y disponible en el historial. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

---

### RF-06 — Persistencia de documentos en MongoDB

| Campo | Descripción |
|---|---|
| **ID** | RF-06 |
| **Nombre** | Persistencia de documentos en MongoDB |
| **Descripción** | El sistema almacena en MongoDB el contenido procesado de los archivos cargados para su consulta y referencia posterior. |
| **Actor(es)** | Sistema (automático) |
| **Precondiciones** | MongoDB debe estar disponible. El usuario debe haber cargado un archivo. |
| **Flujo principal** | 1. El usuario carga un archivo. 2. El sistema extrae el contenido del archivo. 3. El sistema crea un documento en la colección `archivos` de MongoDB con los campos: nombre, tipo, contenido e id_conversacion. 4. El sistema confirma el almacenamiento. |
| **Flujos alternativos** | 3a. Si MongoDB no está disponible, el sistema registra el error y continúa operando con SQLite únicamente. |
| **Postcondiciones** | El contenido del archivo queda almacenado en MongoDB referenciado por id_conversacion. |
| **Prioridad** | Alta |
| **Estabilidad** | Media |

---

### RF-07 — Consultar historial de conversaciones

| Campo | Descripción |
|---|---|
| **ID** | RF-07 |
| **Nombre** | Consultar historial de conversaciones |
| **Descripción** | El sistema permite al usuario visualizar el historial de conversaciones previas almacenadas en la base de datos. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | El usuario debe haber iniciado sesión y tener al menos una conversación guardada. |
| **Flujo principal** | 1. El usuario selecciona la opción "Historial" en el menú lateral. 2. El sistema consulta SQLite y recupera las conversaciones del usuario. 3. El sistema muestra la lista de conversaciones con fecha y nombre del archivo. 4. El usuario selecciona una conversación. 5. El sistema muestra los mensajes de esa conversación. |
| **Flujos alternativos** | 2a. Si no hay conversaciones guardadas, el sistema muestra un mensaje informativo. |
| **Postcondiciones** | El usuario puede revisar el contenido de conversaciones anteriores. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

---

### RF-08 — Exportar conversación a JSON

| Campo | Descripción |
|---|---|
| **ID** | RF-08 |
| **Nombre** | Exportar conversación a JSON |
| **Descripción** | El sistema permite al usuario exportar la conversación activa o una conversación del historial en formato JSON. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | Debe existir al menos una conversación con mensajes. |
| **Flujo principal** | 1. El usuario selecciona "Exportar" en el menú. 2. El usuario elige el formato JSON. 3. El sistema serializa la conversación en formato JSON. 4. El sistema abre el explorador para que el usuario elija la ubicación de guardado. 5. El sistema guarda el archivo y confirma la exportación. |
| **Flujos alternativos** | 3a. Si la conversación está vacía, el sistema notifica que no hay datos para exportar. |
| **Postcondiciones** | Se genera un archivo .json con el contenido de la conversación. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

---

### RF-09 — Exportar conversación a XML

| Campo | Descripción |
|---|---|
| **ID** | RF-09 |
| **Nombre** | Exportar conversación a XML |
| **Descripción** | El sistema permite al usuario exportar la conversación activa o una conversación del historial en formato XML. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | Debe existir al menos una conversación con mensajes. |
| **Flujo principal** | 1. El usuario selecciona "Exportar" en el menú. 2. El usuario elige el formato XML. 3. El sistema serializa la conversación en formato XML con estructura jerárquica. 4. El sistema abre el explorador para que el usuario elija la ubicación de guardado. 5. El sistema guarda el archivo y confirma la exportación. |
| **Flujos alternativos** | 3a. Si la conversación está vacía, el sistema notifica que no hay datos para exportar. |
| **Postcondiciones** | Se genera un archivo .xml con el contenido de la conversación. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

---

### RF-10 — Cerrar Sesión

| Campo | Descripción |
|---|---|
| **ID** | RF-10 |
| **Nombre** | Cerrar Sesión |
| **Descripción** | El sistema permite al usuario cerrar su sesión activa de forma segura, limpiando los datos de la sesión en memoria. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | El usuario debe tener una sesión activa. |
| **Flujo principal** | 1. El usuario hace clic en "Cerrar sesión". 2. El sistema solicita confirmación. 3. El usuario confirma. 4. El sistema limpia los datos de sesión en memoria. 5. El sistema redirige al usuario a la pantalla de inicio de sesión. |
| **Flujos alternativos** | 3a. Si el usuario cancela, el sistema regresa a la pantalla principal sin cambios. |
| **Postcondiciones** | La sesión queda cerrada y los datos sensibles son eliminados de memoria. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

---

## 2. Requerimientos no funcionales

### RNF-01 — Rendimiento del sistema

| Campo | Descripción |
|---|---|
| **ID** | RNF-01 |
| **Nombre** | Rendimiento del sistema |
| **Descripción** | El sistema debe responder a las consultas del usuario en un tiempo máximo aceptable para garantizar una experiencia fluida. |
| **Criterio de aceptación** | El tiempo de respuesta del módulo de IA no debe superar los 5 segundos. La carga de archivos de hasta 5 MB no debe tardar más de 3 segundos. |
| **Métrica** | Tiempo de respuesta medido en segundos desde el envío de la pregunta hasta la visualización de la respuesta. |
| **Prioridad** | Alta |
| **Estabilidad** | Media |

---

### RNF-02 — Seguridad de datos

| Campo | Descripción |
|---|---|
| **ID** | RNF-02 |
| **Nombre** | Seguridad de datos |
| **Descripción** | El sistema debe proteger las credenciales del usuario y los datos almacenados mediante mecanismos básicos de seguridad. |
| **Criterio de aceptación** | Las contraseñas deben almacenarse con hash SHA-256 o equivalente. Las API Keys deben gestionarse mediante archivo .env. No se permite texto plano en ningún momento. |
| **Métrica** | Verificación de que ninguna contraseña se almacena en texto plano en la base de datos. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

---

### RNF-03 — Usabilidad de la interfaz

| Campo | Descripción |
|---|---|
| **ID** | RNF-03 |
| **Nombre** | Usabilidad de la interfaz |
| **Descripción** | La interfaz gráfica debe ser intuitiva y fácil de usar para usuarios con conocimientos básicos de informática. |
| **Criterio de aceptación** | Un usuario nuevo debe completar el flujo principal en menos de 2 minutos sin instrucciones adicionales. Los mensajes de error deben ser claros y orientados al usuario. |
| **Métrica** | Prueba de usabilidad con al menos 2 usuarios externos que logren completar el flujo sin asistencia. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

---

### RNF-04 — Portabilidad del sistema

| Campo | Descripción |
|---|---|
| **ID** | RNF-04 |
| **Nombre** | Portabilidad del sistema |
| **Descripción** | El sistema debe poder ejecutarse en los principales sistemas operativos de escritorio sin modificaciones al código fuente. |
| **Criterio de aceptación** | La aplicación debe funcionar correctamente en Windows 10/11 y Ubuntu 20.04+ con Python 3.10 o superior instalado. |
| **Métrica** | Ejecución exitosa del flujo principal en ambos sistemas operativos. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

---

### RNF-05 — Mantenibilidad del código

| Campo | Descripción |
|---|---|
| **ID** | RNF-05 |
| **Nombre** | Mantenibilidad del código |
| **Descripción** | El código fuente debe estar organizado de forma modular, documentado y seguir convenciones de estilo para facilitar su mantenimiento y extensión futura. |
| **Criterio de aceptación** | El proyecto debe seguir la estructura MVC. Cada módulo debe tener docstrings. El código debe cumplir con PEP 8. El repositorio debe tener un README.md actualizado. |
| **Métrica** | Validación con flake8 con 0 errores críticos. Revisión de estructura de carpetas y presencia de docstrings. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

---

### RNF-06 — Disponibilidad offline

| Campo | Descripción |
|---|---|
| **ID** | RNF-06 |
| **Nombre** | Disponibilidad offline |
| **Descripción** | La aplicación debe funcionar en modo offline para las funcionalidades que no requieran IA externa. |
| **Criterio de aceptación** | Sin conexión a internet, el sistema debe permitir: login, carga de archivos, simulación de respuestas, consulta de historial y exportación. |
| **Métrica** | Ejecución del flujo principal sin conexión a internet activa. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

---

### RNF-07 — Plataforma de desarrollo

| Campo | Descripción |
|---|---|
| **ID** | RNF-07 |
| **Nombre** | Plataforma de desarrollo |
| **Descripción** | La aplicación debe desarrollarse exclusivamente en Python 3.10 o superior. |
| **Criterio de aceptación** | Todo el código fuente debe ser Python. No se permite el uso de otros lenguajes de programación para la lógica principal. |
| **Métrica** | Revisión del repositorio: todos los archivos de lógica deben tener extensión .py. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

---

## 3. Resumen de requerimientos

| ID | Nombre | Tipo | Prioridad |
|---|---|---|---|
| RF-01 | Iniciar Sesión | Funcional | Alta |
| RF-02 | Interfaz tipo chat | Funcional | Alta |
| RF-03 | Carga de archivos | Funcional | Alta |
| RF-04 | Consulta al sistema | Funcional | Alta |
| RF-05 | Persistencia en SQLite | Funcional | Alta |
| RF-06 | Persistencia en MongoDB | Funcional | Alta |
| RF-07 | Consultar historial | Funcional | Media |
| RF-08 | Exportar a JSON | Funcional | Media |
| RF-09 | Exportar a XML | Funcional | Media |
| RF-10 | Cerrar Sesión | Funcional | Alta |
| RNF-01 | Rendimiento | No funcional | Alta |
| RNF-02 | Seguridad | No funcional | Alta |
| RNF-03 | Usabilidad | No funcional | Alta |
| RNF-04 | Portabilidad | No funcional | Media |
| RNF-05 | Mantenibilidad | No funcional | Media |
| RNF-06 | Disponibilidad offline | No funcional | Media |
| RNF-07 | Plataforma Python | No funcional | Alta |

---

## Observación final

Este documento sirve como base para la matriz de trazabilidad, los casos de prueba, el diseño UML y la implementación del sistema. Cualquier cambio en los requerimientos debe reflejarse en todos los documentos relacionados para mantener la coherencia del proyecto.
