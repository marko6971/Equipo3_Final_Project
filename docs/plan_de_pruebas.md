# Plan de Pruebas de Software

**Sistema:** Sistema de Chat con IA para Consulta de Archivos  
**Versión:** 1.0  
**Fecha:** 28/04/2026  
**Autor:** Jorge Edwin Guevara Ayala  
**Estándar:** IEEE 829 — Standard for Software Test Documentation

---

## 1. Introducción

Este documento define el Plan de Pruebas del sistema conforme al estándar IEEE 829. Su propósito es establecer el alcance, enfoque, recursos y calendario de las actividades de prueba, así como identificar los elementos a probar, las características a verificar y los criterios de éxito y fracaso.

### 1.1 Propósito
Garantizar que el sistema cumple con todos los requerimientos funcionales (RF-01 a RF-08) y no funcionales (RNF-01 a RNF-05) antes de su entrega final.

### 1.2 Alcance
El plan cubre los módulos: Autenticación, Carga de Archivos, Chat e IA, Persistencia (SQLite), Historial, Exportación (JSON/XML) e Interfaz Gráfica.

### 1.3 Referencias
- `docs/ejemplos_tdcu.md`
- `docs/matriz_trazabilidad.md`
- `docs/casos_prueba.md`
- `docs/especificacion_suplementaria.md`
- `docs/glosario.md`
- IEEE 829 — Standard for Software Test Documentation

---

## 2. Elementos a Probar

| Componente | Descripción | Tipo de Prueba |
|---|---|---|
| auth.py | Módulo de autenticación de usuarios | Unitaria / Integración |
| file_loader.py | Carga y lectura de archivos TXT y PDF | Unitaria / Funcional |
| chat_ui.py | Interfaz gráfica del chat | Funcional / Usabilidad |
| ia_service.py | Conexión y consulta al servicio de IA | Integración / Rendimiento |
| database.py | Operaciones CRUD en SQLite | Unitaria / Integración |
| history.py | Consulta del historial de conversaciones | Funcional |
| exporter.py | Exportación a JSON y XML | Funcional / Unitaria |
| Sistema completo | Flujo end-to-end del sistema | Sistema / Aceptación |

---

## 3. Características a Probar

| ID Req | Característica | Prioridad | Tipo de Prueba |
|---|---|---|---|
| RF-01 | Autenticación con credenciales válidas e inválidas | Alta | Funcional |
| RF-02 | Carga de archivos TXT y PDF válidos e inválidos | Alta | Funcional |
| RF-03 | Envío de preguntas y recepción de respuestas de IA | Alta | Integración |
| RF-04 | Persistencia de conversaciones en SQLite | Alta | Integración |
| RF-05 | Visualización del historial de conversaciones | Media | Funcional |
| RF-06 | Exportación correcta a formato JSON | Media | Funcional |
| RF-07 | Exportación correcta a formato XML | Media | Funcional |
| RF-08 | Cierre de sesión y limpieza de datos en memoria | Alta | Funcional |
| RNF-01 | Tiempo de respuesta menor a 5 segundos | Alta | Rendimiento |
| RNF-02 | Contraseñas almacenadas con hash SHA-256 | Alta | Seguridad |
| RNF-03 | Flujo principal completado sin asistencia | Alta | Usabilidad |
| RNF-04 | Ejecución en Windows, macOS y Linux | Media | Portabilidad |
| RNF-05 | Código con PEP 8 y estructura modular | Media | Mantenibilidad |

---

## 4. Estrategia de Pruebas

### 4.1 Pruebas Unitarias
Se probarán de forma aislada las funciones y métodos de cada módulo usando **pytest**. Cada función crítica debe tener al menos un caso positivo y uno negativo.

### 4.2 Pruebas de Integración
Se verificará la comunicación entre módulos: `auth.py` ↔ `database.py`, `ia_service.py` ↔ `chat_ui.py`, `exporter.py` ↔ `database.py`.

### 4.3 Pruebas Funcionales
Se validará que cada RF (RF-01 a RF-08) se cumple desde la perspectiva del usuario, siguiendo los flujos definidos en las TDCU.

### 4.4 Pruebas de Rendimiento
Se medirá el tiempo de respuesta con la librería `time` de Python. Criterio: IA < 5s, carga de archivo < 3s.

### 4.5 Pruebas de Seguridad
Se inspeccionará la tabla `usuarios` en SQLite para confirmar que las contraseñas están almacenadas como hash SHA-256.

### 4.6 Pruebas de Usabilidad
Prueba con 2 usuarios externos. Meta: completar flujo principal en menos de 2 minutos sin instrucciones.

### 4.7 Pruebas de Aceptación
Demostración al cliente (profesor) usando la lista de requerimientos como checklist de verificación.

---

## 5. Casos de Prueba Detallados

### CP-01 — Inicio de sesión con credenciales válidas

| Campo | Detalle |
|---|---|
| **ID** | CP-01 |
| **Requerimiento** | RF-01 |
| **Tipo de Prueba** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | El usuario "admin" existe en la BD con contraseña "1234". |
| **Pasos** | 1. Abrir la app. 2. Ingresar usuario: admin. 3. Ingresar contraseña: 1234. 4. Clic en "Iniciar sesión". |
| **Resultado Esperado** | El sistema muestra la pantalla principal con el nombre del usuario. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-02 — Inicio de sesión con credenciales inválidas

| Campo | Detalle |
|---|---|
| **ID** | CP-02 |
| **Requerimiento** | RF-01 |
| **Tipo de Prueba** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | El usuario "admin" existe en la BD. |
| **Pasos** | 1. Abrir la app. 2. Ingresar usuario: admin. 3. Ingresar contraseña: "xxxx". 4. Clic en "Iniciar sesión". |
| **Resultado Esperado** | El sistema muestra mensaje de error. No concede acceso. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-03 — Carga de archivo TXT válido

| Campo | Detalle |
|---|---|
| **ID** | CP-03 |
| **Requerimiento** | RF-02 |
| **Tipo de Prueba** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | Usuario autenticado. Existe "prueba.txt" con contenido. |
| **Pasos** | 1. Clic en "Cargar archivo". 2. Seleccionar "prueba.txt". 3. Confirmar. |
| **Resultado Esperado** | El sistema muestra el nombre del archivo activo y habilita el campo de preguntas. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-04 — Carga de archivo con formato no soportado

| Campo | Detalle |
|---|---|
| **ID** | CP-04 |
| **Requerimiento** | RF-02 |
| **Tipo de Prueba** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | Usuario autenticado. |
| **Pasos** | 1. Clic en "Cargar archivo". 2. Seleccionar un archivo ".xlsx". 3. Confirmar. |
| **Resultado Esperado** | El sistema muestra: "Formato no soportado. Use TXT o PDF." |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-05 — Envío de pregunta con archivo cargado

| Campo | Detalle |
|---|---|
| **ID** | CP-05 |
| **Requerimiento** | RF-03 |
| **Tipo de Prueba** | Integración |
| **Prioridad** | Alta |
| **Precondición** | Usuario autenticado con archivo TXT cargado. |
| **Pasos** | 1. Escribir pregunta relacionada al archivo. 2. Presionar "Enviar". |
| **Resultado Esperado** | El sistema muestra la respuesta de la IA en el área del chat. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-06 — Envío de pregunta sin archivo cargado

| Campo | Detalle |
|---|---|
| **ID** | CP-06 |
| **Requerimiento** | RF-03 |
| **Tipo de Prueba** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | Usuario autenticado. Sin archivo cargado. |
| **Pasos** | 1. Escribir pregunta. 2. Presionar "Enviar". |
| **Resultado Esperado** | El sistema muestra aviso: "Debe cargar un archivo antes de hacer preguntas." |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-07 — Persistencia de conversación en SQLite

| Campo | Detalle |
|---|---|
| **ID** | CP-07 |
| **Requerimiento** | RF-04 |
| **Tipo de Prueba** | Integración |
| **Prioridad** | Alta |
| **Precondición** | El usuario realizó al menos una pregunta con respuesta. |
| **Pasos** | 1. Enviar pregunta y recibir respuesta. 2. Cerrar la app. 3. Reabrir. 4. Consultar historial. |
| **Resultado Esperado** | La conversación anterior aparece en el historial con fecha, pregunta y respuesta. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-08 — Consulta del historial de conversaciones

| Campo | Detalle |
|---|---|
| **ID** | CP-08 |
| **Requerimiento** | RF-05 |
| **Tipo de Prueba** | Funcional |
| **Prioridad** | Media |
| **Precondición** | El usuario tiene al menos 2 conversaciones guardadas. |
| **Pasos** | 1. Clic en "Historial". 2. Seleccionar una conversación. |
| **Resultado Esperado** | El sistema muestra los mensajes con fecha y archivo asociado. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-09 — Exportación de conversación a JSON

| Campo | Detalle |
|---|---|
| **ID** | CP-09 |
| **Requerimiento** | RF-06 |
| **Tipo de Prueba** | Funcional |
| **Prioridad** | Media |
| **Precondición** | Existe una conversación con al menos 2 mensajes. |
| **Pasos** | 1. Seleccionar "Exportar". 2. Elegir JSON. 3. Seleccionar ruta. 4. Confirmar. |
| **Resultado Esperado** | Se genera un archivo .json con estructura correcta: usuario, fecha, mensajes. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-10 — Exportación de conversación a XML

| Campo | Detalle |
|---|---|
| **ID** | CP-10 |
| **Requerimiento** | RF-07 |
| **Tipo de Prueba** | Funcional |
| **Prioridad** | Media |
| **Precondición** | Existe una conversación con al menos 2 mensajes. |
| **Pasos** | 1. Seleccionar "Exportar". 2. Elegir XML. 3. Seleccionar ruta. 4. Confirmar. |
| **Resultado Esperado** | Se genera un archivo .xml con estructura jerárquica válida y bien formada. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-11 — Cierre de sesión

| Campo | Detalle |
|---|---|
| **ID** | CP-11 |
| **Requerimiento** | RF-08 |
| **Tipo de Prueba** | Funcional |
| **Prioridad** | Alta |
| **Precondición** | El usuario tiene una sesión activa. |
| **Pasos** | 1. Clic en "Cerrar sesión". 2. Confirmar en el diálogo. |
| **Resultado Esperado** | El sistema regresa al login. Los datos de sesión son eliminados de memoria. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-12 — Tiempo de respuesta de la IA

| Campo | Detalle |
|---|---|
| **ID** | CP-12 |
| **Requerimiento** | RNF-01 |
| **Tipo de Prueba** | Rendimiento |
| **Prioridad** | Alta |
| **Precondición** | Archivo TXT cargado. Conexión a internet activa. |
| **Pasos** | 1. Registrar tiempo antes de enviar. 2. Enviar pregunta. 3. Registrar tiempo al recibir respuesta. |
| **Resultado Esperado** | El tiempo total de respuesta es menor a 5 segundos. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

### CP-13 — Verificación de hash de contraseñas

| Campo | Detalle |
|---|---|
| **ID** | CP-13 |
| **Requerimiento** | RNF-02 |
| **Tipo de Prueba** | Seguridad |
| **Prioridad** | Alta |
| **Precondición** | El usuario "admin" está registrado en la BD. |
| **Pasos** | 1. Abrir SQLite con DB Browser. 2. Consultar tabla "usuarios". 3. Revisar campo "contraseña". |
| **Resultado Esperado** | El campo muestra un hash de 64 caracteres hexadecimales, no texto plano. |
| **Resultado Obtenido** | _(pendiente)_ |
| **Estado** | Pendiente |

---

## 6. Criterios de Entrada y Salida

### 6.1 Criterios de Entrada
- Código fuente disponible en el repositorio.
- Entorno de pruebas configurado (Python 3.10+, dependencias instaladas).
- Base de datos SQLite inicializada con datos de prueba.
- Documentos de requerimientos y TDCU aprobados.

### 6.2 Criterios de Salida
- 100% de los casos de prueba de prioridad Alta ejecutados.
- 80% o más de los casos de prioridad Media ejecutados.
- Sin defectos críticos abiertos.
- Documento de resultados completo.

---

## 7. Entorno de Pruebas

| Componente | Especificación |
|---|---|
| Sistema Operativo | Windows 10/11 (principal), Ubuntu 20.04 (portabilidad) |
| Lenguaje | Python 3.10+ |
| Framework de Pruebas | pytest 7.x |
| Base de Datos | SQLite 3 |
| Visor de BD | DB Browser for SQLite |
| Editor | Visual Studio Code |
| Control de Versiones | Git + GitHub (EddGuev/Equipo3_Final_Project) |
| Archivos de Prueba | prueba.txt, prueba.pdf (en /tests/data/) |

---

## 8. Roles y Responsabilidades

| Rol | Responsabilidad | Responsable |
|---|---|---|
| Líder de Pruebas | Planificar, coordinar y revisar resultados | Jorge Edwin Guevara Ayala |
| Ejecutor de Pruebas | Ejecutar casos y registrar resultados | Equipo de Desarrollo |
| Revisor de Calidad | Validar criterios de salida | Equipo de Desarrollo |
| Cliente / Evaluador | Aprobar pruebas de aceptación | Profesor (cliente) |

---

## 9. Calendario de Pruebas

| Fase | Actividad | Duración | Responsable |
|---|---|---|---|
| Preparación | Configurar entorno y datos de prueba | 1 día | Equipo |
| Pruebas Unitarias | CP-01 a CP-04 | 2 días | Equipo |
| Pruebas de Integración | CP-05, CP-07 | 2 días | Equipo |
| Pruebas Funcionales | CP-06, CP-08 a CP-11 | 2 días | Equipo |
| Pruebas No Funcionales | CP-12, CP-13 | 1 día | Equipo |
| Pruebas de Aceptación | Demostración al cliente | 1 día | Equipo + Profesor |
| Cierre | Documentar resultados y defectos | 1 día | Equipo |

---

## 10. Gestión de Defectos

| Campo | Descripción |
|---|---|
| ID Defecto | DEF-001, DEF-002, ... |
| Caso de Prueba | ID del caso donde se encontró |
| Descripción | Comportamiento incorrecto observado |
| Severidad | Crítico / Alto / Medio / Bajo |
| Pasos para reproducir | Secuencia exacta |
| Resultado Obtenido | Lo que ocurrió |
| Resultado Esperado | Lo que debería ocurrir |
| Estado | Abierto / En corrección / Resuelto / Cerrado |
| Responsable | Persona asignada |

### 10.1 Clasificación de Severidad

| Severidad | Descripción | Tiempo de Resolución |
|---|---|---|
| Crítico | El sistema no puede ejecutarse o pierde datos | Inmediato (mismo día) |
| Alto | Una funcionalidad principal no opera correctamente | 1-2 días |
| Medio | Una funcionalidad secundaria falla | 3-5 días |
| Bajo | Problema cosmético o de usabilidad menor | Antes de entrega final |

---

## 11. Métricas de Prueba

| Métrica | Fórmula / Descripción | Meta |
|---|---|---|
| Cobertura de Casos | Casos ejecutados / Total × 100 | ≥ 90% |
| Tasa de Éxito | Casos aprobados / Ejecutados × 100 | ≥ 85% |
| Densidad de Defectos | Total defectos / Módulos probados | < 2 por módulo |
| Defectos Críticos Abiertos | Conteo sin resolver | 0 al cierre |
| Tiempo Promedio de Respuesta | Promedio medido en CP-12 | < 5 segundos |

---

## 12. Aprobación del Documento

| Rol | Nombre | Firma | Fecha |
|---|---|---|---|
| Autor / Líder de Pruebas | Jorge Edwin Guevara Ayala | _______________ | 28/04/2026 |
| Revisor | | _______________ | |
| Cliente / Evaluador | | _______________ | |