# Documentación de Requerimientos y TDCU

**Sistema:** Sistema de Chat con IA para Consulta de Archivos  
**Versión:** 1.0  
**Fecha:** 28/04/2026  
**Autor:** Jorge Edwin Guevara Ayala

## Propósito
Este documento describe los requerimientos funcionales y no funcionales del sistema, así como sus Tablas de Descripción de Casos de Uso (TDCU), para apoyar la planeación, diseño, implementación y validación del proyecto conforme a prácticas de Ingeniería de Software.

## Alcance
El sistema permitirá a un usuario autenticarse, cargar archivos TXT o PDF, realizar preguntas sobre su contenido mediante un chat asistido por IA, almacenar conversaciones en SQLite y exportarlas a JSON y XML.

## 1. Requerimientos funcionales

### RF-01 — Iniciar Sesión

| Campo | Descripción |
|---|---|
| **ID** | RF-01 |
| **Nombre** | Iniciar Sesión |
| **Descripción** | El sistema permite al usuario autenticarse mediante nombre de usuario y contraseña para acceder a las funcionalidades del sistema. |
| **Actor(es)** | Usuario registrado |
| **Precondiciones** | El usuario debe estar registrado en el sistema. La base de datos debe estar disponible. |
| **Flujo principal** | 1. El usuario abre la aplicación. 2. El sistema muestra el formulario de inicio de sesión. 3. El usuario ingresa su nombre de usuario y contraseña. 4. El sistema valida las credenciales contra la base de datos. 5. El sistema concede acceso y muestra la pantalla principal. |
| **Flujos alternativos** | 4a. Si las credenciales son incorrectas, el sistema muestra un mensaje de error y permite reintentar. |
| **Postcondiciones** | El usuario queda autenticado y puede usar el sistema. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

### RF-02 — Cargar Archivo

| Campo | Descripción |
|---|---|
| **ID** | RF-02 |
| **Nombre** | Cargar Archivo |
| **Descripción** | El sistema permite al usuario cargar un archivo en formato TXT o PDF para ser procesado y consultado mediante el chat. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | El usuario debe haber iniciado sesión. El archivo debe ser de tipo TXT o PDF. |
| **Flujo principal** | 1. El usuario hace clic en "Cargar archivo". 2. El sistema abre el explorador de archivos. 3. El usuario selecciona un archivo TXT o PDF. 4. El sistema lee y procesa el contenido del archivo. 5. El sistema confirma la carga exitosa y muestra el nombre del archivo activo. |
| **Flujos alternativos** | 3a. Si el archivo no es TXT ni PDF, el sistema muestra un mensaje de formato no soportado. 4a. Si el archivo está vacío o corrupto, el sistema notifica al usuario. |
| **Postcondiciones** | El contenido del archivo queda disponible para ser consultado en el chat. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

### RF-03 — Enviar Pregunta al Chat

| Campo | Descripción |
|---|---|
| **ID** | RF-03 |
| **Nombre** | Enviar Pregunta al Chat |
| **Descripción** | El sistema permite al usuario escribir y enviar preguntas relacionadas con el contenido del archivo cargado, recibiendo una respuesta generada por el módulo de IA. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | El usuario debe haber iniciado sesión y tener un archivo cargado. |
| **Flujo principal** | 1. El usuario escribe una pregunta en el campo de texto. 2. El usuario presiona "Enviar" o la tecla Enter. 3. El sistema envía la pregunta junto con el contenido del archivo al módulo de IA. 4. El módulo de IA genera una respuesta. 5. El sistema muestra la respuesta en el área del chat. |
| **Flujos alternativos** | 2a. Si el campo está vacío, el sistema no procesa la solicitud. 3a. Si no hay archivo cargado, el sistema muestra un aviso al usuario. 4a. Si el servicio de IA no responde, el sistema muestra un mensaje de error. |
| **Postcondiciones** | La pregunta y la respuesta quedan registradas en la conversación activa. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

### RF-04 — Guardar Conversación en Base de Datos

| Campo | Descripción |
|---|---|
| **ID** | RF-04 |
| **Nombre** | Guardar Conversación en Base de Datos |
| **Descripción** | El sistema almacena automáticamente cada conversación (preguntas y respuestas) en la base de datos SQLite, asociada al usuario y al archivo consultado. |
| **Actor(es)** | Sistema (automático) |
| **Precondiciones** | El usuario debe estar autenticado y haber enviado al menos un mensaje. |
| **Flujo principal** | 1. El usuario envía un mensaje. 2. El sistema recibe la respuesta de la IA. 3. El sistema guarda el par pregunta-respuesta en la tabla Mensaje. 4. El sistema asocia el mensaje a la conversación activa en la tabla Conversacion. |
| **Flujos alternativos** | 3a. Si la base de datos no está disponible, el sistema registra el error en un log y notifica al usuario. |
| **Postcondiciones** | El mensaje queda persistido en la base de datos y disponible en el historial. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

### RF-05 — Consultar Historial de Conversaciones

| Campo | Descripción |
|---|---|
| **ID** | RF-05 |
| **Nombre** | Consultar Historial de Conversaciones |
| **Descripción** | El sistema permite al usuario visualizar el historial de conversaciones previas almacenadas en la base de datos. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | El usuario debe haber iniciado sesión y tener al menos una conversación guardada. |
| **Flujo principal** | 1. El usuario selecciona la opción "Historial" en el menú lateral. 2. El sistema consulta la base de datos y recupera las conversaciones del usuario. 3. El sistema muestra la lista de conversaciones con fecha y nombre del archivo. 4. El usuario selecciona una conversación. 5. El sistema muestra los mensajes de esa conversación. |
| **Flujos alternativos** | 2a. Si no hay conversaciones guardadas, el sistema muestra un mensaje informativo. |
| **Postcondiciones** | El usuario puede revisar el contenido de conversaciones anteriores. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

### RF-06 — Exportar Conversación a JSON

| Campo | Descripción |
|---|---|
| **ID** | RF-06 |
| **Nombre** | Exportar Conversación a JSON |
| **Descripción** | El sistema permite al usuario exportar la conversación activa o una conversación del historial en formato JSON. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | Debe existir al menos una conversación con mensajes. |
| **Flujo principal** | 1. El usuario selecciona "Exportar" en el menú. 2. El usuario elige el formato JSON. 3. El sistema serializa la conversación en formato JSON. 4. El sistema abre el explorador para que el usuario elija la ubicación de guardado. 5. El sistema guarda el archivo y confirma la exportación. |
| **Flujos alternativos** | 3a. Si la conversación está vacía, el sistema notifica que no hay datos para exportar. |
| **Postcondiciones** | Se genera un archivo .json con el contenido de la conversación. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

### RF-07 — Exportar Conversación a XML

| Campo | Descripción |
|---|---|
| **ID** | RF-07 |
| **Nombre** | Exportar Conversación a XML |
| **Descripción** | El sistema permite al usuario exportar la conversación activa o una conversación del historial en formato XML. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | Debe existir al menos una conversación con mensajes. |
| **Flujo principal** | 1. El usuario selecciona "Exportar" en el menú. 2. El usuario elige el formato XML. 3. El sistema serializa la conversación en formato XML con estructura jerárquica. 4. El sistema abre el explorador para que el usuario elija la ubicación de guardado. 5. El sistema guarda el archivo y confirma la exportación. |
| **Flujos alternativos** | 3a. Si la conversación está vacía, el sistema notifica que no hay datos para exportar. |
| **Postcondiciones** | Se genera un archivo .xml con el contenido de la conversación. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

### RF-08 — Cerrar Sesión

| Campo | Descripción |
|---|---|
| **ID** | RF-08 |
| **Nombre** | Cerrar Sesión |
| **Descripción** | El sistema permite al usuario cerrar su sesión activa de forma segura, limpiando los datos de la sesión en memoria. |
| **Actor(es)** | Usuario autenticado |
| **Precondiciones** | El usuario debe tener una sesión activa. |
| **Flujo principal** | 1. El usuario hace clic en "Cerrar sesión". 2. El sistema solicita confirmación. 3. El usuario confirma. 4. El sistema limpia los datos de sesión en memoria. 5. El sistema redirige al usuario a la pantalla de inicio de sesión. |
| **Flujos alternativos** | 3a. Si el usuario cancela, el sistema regresa a la pantalla principal sin cambios. |
| **Postcondiciones** | La sesión queda cerrada y los datos sensibles son eliminados de memoria. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

## 2. Requerimientos no funcionales

### RNF-01 — Rendimiento del sistema

| Campo | Descripción |
|---|---|
| **ID** | RNF-01 |
| **Nombre** | Rendimiento del sistema |
| **Descripción** | El sistema debe responder a las consultas del usuario en un tiempo máximo aceptable para garantizar una experiencia fluida. |
| **Criterio de aceptación** | El tiempo de respuesta del módulo de IA no debe superar los 5 segundos en condiciones normales de operación. La carga de archivos TXT/PDF de hasta 10 MB no debe tardar más de 3 segundos. |
| **Métrica** | Tiempo de respuesta medido en segundos desde el envío de la pregunta hasta la visualización de la respuesta. |
| **Prioridad** | Alta |
| **Estabilidad** | Media |

### RNF-02 — Seguridad de datos

| Campo | Descripción |
|---|---|
| **ID** | RNF-02 |
| **Nombre** | Seguridad de datos |
| **Descripción** | El sistema debe proteger las credenciales del usuario y los datos almacenados en la base de datos mediante mecanismos básicos de seguridad. |
| **Criterio de aceptación** | Las contraseñas deben almacenarse con hash SHA-256 o equivalente. No deben mostrarse en texto plano en ningún momento. El acceso a la base de datos debe estar restringido al proceso de la aplicación. |
| **Métrica** | Verificación de que ninguna contraseña se almacena en texto plano en la base de datos. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

### RNF-03 — Usabilidad de la interfaz

| Campo | Descripción |
|---|---|
| **ID** | RNF-03 |
| **Nombre** | Usabilidad de la interfaz |
| **Descripción** | La interfaz gráfica debe ser intuitiva y fácil de usar, permitiendo que un usuario sin conocimientos técnicos pueda operar el sistema sin necesidad de capacitación previa. |
| **Criterio de aceptación** | Un usuario nuevo debe ser capaz de cargar un archivo y realizar una consulta en menos de 2 minutos sin instrucciones adicionales. Los mensajes de error deben ser claros y orientados al usuario. |
| **Métrica** | Prueba de usabilidad con al menos 2 usuarios externos que logren completar el flujo principal sin asistencia. |
| **Prioridad** | Alta |
| **Estabilidad** | Alta |

### RNF-04 — Portabilidad del sistema

| Campo | Descripción |
|---|---|
| **ID** | RNF-04 |
| **Nombre** | Portabilidad del sistema |
| **Descripción** | El sistema debe poder ejecutarse en los principales sistemas operativos de escritorio sin modificaciones al código fuente. |
| **Criterio de aceptación** | La aplicación debe funcionar correctamente en Windows 10/11, macOS 12+ y Ubuntu 20.04+ con Python 3.10 o superior instalado. |
| **Métrica** | Ejecución exitosa del flujo principal en los 3 sistemas operativos mencionados. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

### RNF-05 — Mantenibilidad del código

| Campo | Descripción |
|---|---|
| **ID** | RNF-05 |
| **Nombre** | Mantenibilidad del código |
| **Descripción** | El código fuente debe estar organizado de forma modular, documentado y seguir convenciones de estilo para facilitar su mantenimiento y extensión futura. |
| **Criterio de aceptación** | El proyecto debe seguir la estructura MVC o equivalente. Cada módulo debe tener docstrings. El código debe cumplir con PEP 8. El repositorio debe tener un README.md actualizado. |
| **Métrica** | Revisión de estructura de carpetas, presencia de docstrings y validación con pylint con puntaje mínimo de 7/10. |
| **Prioridad** | Media |
| **Estabilidad** | Alta |

## 3. Resumen de requerimientos

| ID | Nombre | Tipo | Prioridad |
|---|---|---|---|
| RF-01 | Iniciar Sesión | Funcional | Alta |
| RF-02 | Cargar Archivo | Funcional | Alta |
| RF-03 | Enviar Pregunta al Chat | Funcional | Alta |
| RF-04 | Guardar Conversación | Funcional | Alta |
| RF-05 | Consultar Historial | Funcional | Media |
| RF-06 | Exportar a JSON | Funcional | Media |
| RF-07 | Exportar a XML | Funcional | Media |
| RF-08 | Cerrar Sesión | Funcional | Alta |
| RNF-01 | Rendimiento | No funcional | Alta |
| RNF-02 | Seguridad | No funcional | Alta |
| RNF-03 | Usabilidad | No funcional | Alta |
| RNF-04 | Portabilidad | No funcional | Media |
| RNF-05 | Mantenibilidad | No funcional | Media |

## Observación final
Este documento sirve como base para la matriz de trazabilidad, los casos de prueba, el diseño UML y la implementación del sistema.