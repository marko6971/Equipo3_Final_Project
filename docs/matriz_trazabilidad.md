# Matriz de Trazabilidad

**Proyecto:** Aplicación de Chat con IA sobre archivos  
**Versión:** 2.0  
**Fecha:** 28/04/2026  
**Equipo:** Equipo 3  

---

## 1. Introducción

Este documento relaciona cada requerimiento del sistema con su caso de uso correspondiente, el módulo de código que lo implementará y el caso de prueba que lo valida. Su propósito es garantizar que ningún requerimiento quede sin implementación ni sin prueba.

---

## 2. Matriz de trazabilidad

| ID Req | Tipo | Descripción | Caso de Uso | Módulo (futuro) | Caso de Prueba |
|:---|:---|:---|:---|:---|:---|
| RF-01 | Funcional | Inicio de sesión | CU-01 | `auth.py` | CP-01, CP-02 |
| RF-02 | Funcional | Interfaz tipo chat | CU-03 | `chat_ui.py` | CP-06, CP-07 |
| RF-03 | Funcional | Carga de archivos TXT, PDF, JSON, XML | CU-02 | `file_loader.py` | CP-03, CP-04, CP-05 |
| RF-04 | Funcional | Consulta al sistema (IA o simulación) | CU-03 | `ia_service.py` | CP-06, CP-07 |
| RF-05 | Funcional | Persistencia de conversaciones en SQLite | CU-04 | `database.py` | CP-08 |
| RF-06 | Funcional | Persistencia de documentos en MongoDB | CU-04 | `mongo_service.py` | CP-09 |
| RF-07 | Funcional | Consulta de historial de conversaciones | CU-05 | `history.py` | CP-10 |
| RF-08 | Funcional | Exportación a JSON | CU-06 | `exporter.py` | CP-11 |
| RF-09 | Funcional | Exportación a XML | CU-06 | `exporter.py` | CP-12 |
| RF-10 | Funcional | Cierre de sesión | CU-07 | `auth.py` | CP-13 |
| RNF-01 | No funcional | Rendimiento (respuesta < 5 segundos) | — | Sistema general | CP-14 |
| RNF-02 | No funcional | Seguridad (hash de contraseñas, .env) | — | `auth.py` / `database.py` | CP-15 |
| RNF-03 | No funcional | Usabilidad (flujo sin asistencia) | — | Interfaz gráfica | CP-16 |
| RNF-04 | No funcional | Portabilidad (Windows y Linux) | — | Sistema general | CP-17 |
| RNF-05 | No funcional | Mantenibilidad (PEP 8, docstrings) | — | Estructura del proyecto | CP-18 |
| RNF-06 | No funcional | Disponibilidad offline | — | Sistema general | — |
| RNF-07 | No funcional | Plataforma Python 3.10+ | — | Sistema general | — |

---

## 3. Trazabilidad inversa — Casos de prueba a requerimientos

| Caso de Prueba | Requerimiento validado | Módulo relacionado |
|:---|:---|:---|
| CP-01 | RF-01 | `auth.py` |
| CP-02 | RF-01 | `auth.py` |
| CP-03 | RF-03 | `file_loader.py` |
| CP-04 | RF-03 | `file_loader.py` |
| CP-05 | RF-03 | `file_loader.py` |
| CP-06 | RF-02, RF-04 | `chat_ui.py`, `ia_service.py` |
| CP-07 | RF-02, RF-04 | `chat_ui.py`, `ia_service.py` |
| CP-08 | RF-05 | `database.py` |
| CP-09 | RF-06 | `mongo_service.py` |
| CP-10 | RF-07 | `history.py` |
| CP-11 | RF-08 | `exporter.py` |
| CP-12 | RF-09 | `exporter.py` |
| CP-13 | RF-10 | `auth.py` |
| CP-14 | RNF-01 | Sistema general |
| CP-15 | RNF-02 | `auth.py`, `database.py` |
| CP-16 | RNF-03 | Interfaz gráfica |
| CP-17 | RNF-04 | Sistema general |
| CP-18 | RNF-05 | Estructura del proyecto |

---

## 4. Cobertura de requerimientos

| Total de requerimientos | Con caso de prueba | Sin caso de prueba |
|:---|:---|:---|
| 17 (10 RF + 7 RNF) | 15 | 2 (RNF-06, RNF-07 — validados por configuración) |

---

## 5. Observaciones

- Los módulos listados en la columna **"Módulo (futuro)"** corresponden a la estructura de código planificada en la carpeta `src/` del repositorio.
- RNF-06 (disponibilidad offline) y RNF-07 (plataforma Python) se validan por configuración del entorno, no mediante casos de prueba formales.
- Esta matriz debe actualizarse cada vez que se agregue, modifique o elimine un requerimiento o caso de prueba.
