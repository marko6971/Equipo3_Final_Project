# Especificación Suplementaria

## 1. Introducción
Este documento define los requisitos de calidad, restricciones y estándares técnicos que el sistema de Chat con IA debe cumplir para asegurar su correcto funcionamiento y mantenibilidad.

## 2. Restricciones de Diseño e Implementación
- **Lenguaje de Programación:** Python 3.10 o superior.
- **Interfaz Gráfica:** Uso exclusivo de librerías nativas o estándar (Tkinter o PyQt6).
- **Base de Datos:** SQLite para datos relacionales locales; MongoDB para almacenamiento de documentos (opcional según arquitectura).
- **Arquitectura:** Debe seguir el patrón Modelo-Vista-Controlador (MVC).

## 3. Requisitos de Interfaz Externa
- **Servicios de IA:** Conexión vía API REST a modelos como OpenAI, Groq o similares.
- **Manejo de Archivos:** Soporte para lectura de archivos PDF mediante `pdfplumber` o `PyPDF2` y archivos TXT mediante codificación UTF-8.

## 4. Atributos de Calidad
- **Portabilidad:** El sistema debe ser empaquetable en un ejecutable (.exe) para Windows mediante herramientas como `PyInstaller`.
- **Mantenibilidad:** El código debe estar documentado con Docstrings y seguir la guía de estilo PEP 8.
- **Seguridad:** Las llaves de API (API Keys) no deben estar "hardcodeadas" en el código; deben leerse desde un archivo `.env` o variables de entorno.

## 5. Estándares Aplicados
- **Ingeniería de Software:** Siguiendo lineamientos generales de IEEE 830 para la especificación de requisitos.
- **Persistencia:** Cumplimiento de integridad referencial en la base de datos SQLite.