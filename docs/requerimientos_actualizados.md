# Documento de Levantamiento de Requerimientos

**Proyecto:** Aplicación de Chat con IA sobre archivos  
**Cliente:** Profesor de la materia Ingeniería de Software  
**Equipo:** Equipo 3  
**Versión:** 2.0  
**Fecha:** 28/04/2026  

## 1. Información general

El presente documento describe los requerimientos del sistema para el desarrollo de una aplicación de escritorio en Python que permita cargar archivos, realizar consultas sobre su contenido mediante un servicio de inteligencia artificial o una simulación, almacenar conversaciones en base de datos y exportarlas en formatos estructurados.

## 2. Objetivo del sistema

Desarrollar una aplicación de escritorio tipo chat que permita al usuario interactuar con el contenido de archivos cargados, obtener respuestas a partir de dicho contenido, almacenar el historial de conversaciones y exportar la información en formatos JSON y XML.

## 3. Alcance

### 3.1 Incluye

- Interfaz gráfica tipo chat.
- Sistema de autenticación por usuario y contraseña.
- Carga y procesamiento de archivos TXT, PDF, JSON y XML.
- Consulta al sistema mediante IA o simulación de respuestas.
- Almacenamiento de conversaciones y datos asociados.
- Consulta de historial de conversaciones.
- Exportación de conversaciones en formato JSON y XML.
- Persistencia híbrida con base de datos relacional y no relacional.

### 3.2 No incluye

- Entrenamiento de modelos de inteligencia artificial.
- Desarrollo de una versión web o móvil.
- Integraciones externas complejas fuera del entorno local.

## 4. Stakeholders

- **Cliente:** Profesor de Ingeniería de Software.
- **Usuario final:** Estudiante.
- **Desarrolladores:** Equipo 3.
- **Evaluadores:** Docente y equipo de revisión académica.

## 5. Descripción general de la solución

La solución consistirá en una aplicación de escritorio desarrollada en Python con una interfaz gráfica estilo chat. El usuario podrá iniciar sesión, cargar archivos compatibles, formular preguntas sobre el contenido y recibir respuestas generadas por una IA o por un módulo de simulación.

La información se almacenará mediante una arquitectura híbrida:

- **SQLite** para usuarios, sesiones, conversaciones e historial relacional.
- **MongoDB** para el contenido procesado de documentos y estructuras no relacionales.

## 6. Tecnologías consideradas

- **Lenguaje principal:** Python.
- **Interfaz gráfica:** Tkinter o PyQt.
- **Base de datos relacional:** SQLite.
- **Base de datos no relacional:** MongoDB.
- **Lectura de PDF:** `pdfplumber`.
- **Procesamiento JSON:** `json`.
- **Procesamiento XML:** `xml.etree.ElementTree`.
- **Procesamiento TXT:** lectura directa con Python.

## 7. Requerimientos funcionales

### RF-01. Inicio de sesión
El sistema debe permitir el acceso mediante usuario y contraseña válidos.

### RF-02. Interfaz tipo chat
El sistema debe mostrar una interfaz tipo chat que permita:
- visualizar la conversación completa,
- ingresar preguntas en un campo de texto,
- enviar mensajes mediante un botón,
- diferenciar visualmente los mensajes del usuario y del sistema.

### RF-03. Carga de archivos
El sistema debe permitir seleccionar y cargar archivos desde el sistema local.
Debe mostrar el nombre del archivo cargado y soportar los formatos TXT, PDF, JSON y XML.

### RF-04. Consulta al sistema
El sistema debe permitir al usuario realizar preguntas relacionadas con el contenido del archivo cargado.
Debe responder con base en la información extraída del archivo, ya sea mediante una IA real o una simulación funcional.

### RF-05. Persistencia de conversaciones
El sistema debe guardar automáticamente cada conversación en la base de datos relacional.
Debe registrar al menos:
- identificador de conversación,
- usuario,
- fecha y hora,
- mensajes,
- archivo asociado.

### RF-06. Persistencia de documentos procesados
El sistema debe almacenar en MongoDB el contenido estructurado o extraído de los archivos cargados para su consulta posterior.

### RF-07. Consulta de historial
El sistema debe permitir al usuario consultar el historial de conversaciones previamente almacenadas.

### RF-08. Exportación de conversaciones
El sistema debe permitir exportar conversaciones en formato JSON y XML.

### RF-09. Cierre de sesión
El sistema debe permitir cerrar la sesión activa de forma segura y regresar a la pantalla de autenticación.

## 8. Requerimientos no funcionales

### RNF-01. Plataforma de desarrollo
La aplicación debe desarrollarse en Python.

### RNF-02. Usabilidad
La interfaz gráfica debe ser amigable, clara y fácil de usar para usuarios con conocimientos básicos de informática.

### RNF-03. Persistencia híbrida
El sistema debe utilizar una base de datos relacional (SQLite) y una base de datos no relacional (MongoDB) de acuerdo con la arquitectura definida.

### RNF-04. Rendimiento
El sistema debe responder en menos de 5 segundos en escenarios normales de simulación o consulta local.

### RNF-05. Mantenibilidad
El código debe estar estructurado en módulos, seguir buenas prácticas de programación y facilitar su mantenimiento.

### RNF-06. Portabilidad
La aplicación debe poder ejecutarse en entornos Windows y Linux con los componentes necesarios instalados.

### RNF-07. Seguridad básica
Las credenciales del usuario no deben almacenarse en texto plano y se debe proteger la sesión básica del sistema.

## 9. Casos de uso principales

### CU-01. Iniciar sesión
- El usuario ingresa sus credenciales.
- El sistema valida el acceso.
- El sistema muestra la pantalla principal si las credenciales son correctas.

### CU-02. Cargar archivo
- El usuario selecciona un archivo compatible.
- El sistema valida el formato.
- El sistema registra el archivo y procesa su contenido.

### CU-03. Realizar consulta
- El usuario escribe una pregunta.
- El sistema consulta el contenido del archivo cargado.
- El sistema genera y muestra una respuesta.

### CU-04. Guardar conversación
- El sistema almacena automáticamente la interacción.
- La conversación queda registrada en SQLite.
- El contenido procesado del archivo queda disponible en MongoDB cuando corresponda.

### CU-05. Consultar historial
- El usuario accede al historial.
- El sistema muestra conversaciones previas almacenadas.

### CU-06. Exportar conversación
- El usuario selecciona una conversación.
- El sistema genera un archivo JSON o XML.

### CU-07. Cerrar sesión
- El usuario selecciona la opción de cerrar sesión.
- El sistema finaliza la sesión y vuelve al login.

## 10. Restricciones

- Uso obligatorio de Python.
- Uso obligatorio de base de datos.
- El uso de una API de IA es opcional; puede emplearse simulación.
- El proyecto se desarrollará en tiempo académico limitado.
- La solución debe ser ejecutable en entorno local.

## 11. Supuestos

- El usuario contará con conocimientos básicos para operar la aplicación.
- Los archivos cargados serán válidos y legibles.
- SQLite y MongoDB estarán disponibles en el entorno de desarrollo cuando se requiera la persistencia completa.
- El sistema podrá funcionar con simulación de IA si no se cuenta con una API externa.

## 12. Riesgos

| Riesgo | Impacto | Mitigación |
|---|---|---|
| No contar con API de IA gratuita | Medio | Implementar simulación de respuestas |
| Problemas al extraer texto de PDFs | Alto | Usar `pdfplumber` y archivos TXT como respaldo |
| Inconsistencias entre documentos del proyecto | Medio | Mantener trazabilidad y actualización continua |
| Falta de tiempo de desarrollo | Alto | Priorizar funcionalidades mínimas viables |
| Problemas de configuración de MongoDB | Medio | Preparar pruebas locales y definir almacenamiento alterno temporal |

## 13. Criterios de aceptación generales

- El usuario puede iniciar y cerrar sesión correctamente.
- El sistema carga archivos TXT, PDF, JSON y XML válidos.
- El usuario puede formular preguntas y recibir respuestas.
- Las conversaciones se almacenan correctamente en SQLite.
- Los documentos procesados se almacenan correctamente en MongoDB.
- El historial de conversaciones puede consultarse.
- Las conversaciones pueden exportarse a JSON y XML.

## 14. Observaciones finales

Este documento actualiza y consolida el levantamiento de requerimientos del proyecto para mantener coherencia con la arquitectura, los diagramas y el plan de pruebas ya definidos por el equipo.
