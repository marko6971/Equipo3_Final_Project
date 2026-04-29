CP-01 — Inicio de sesión correcto
Requerimiento: RF-01
Descripción: Validar acceso con credenciales correctas
Entrada: usuario válido + contraseña correcta
Resultado esperado: acceso concedido
CP-02 — Carga de archivo válida
Requerimiento: RF-02
Entrada: archivo PDF o TXT válido
Resultado esperado: archivo cargado correctamente
CP-03 — Envío de pregunta
Requerimiento: RF-03
Entrada: pregunta del usuario
Resultado esperado: respuesta mostrada en chat
CP-04 — Guardado en base de datos
Requerimiento: RF-04
Entrada: pregunta + respuesta
Resultado esperado: registro guardado en SQLite
CP-05 — Consulta de historial
Requerimiento: RF-05
Entrada: usuario con historial
Resultado esperado: lista de conversaciones mostrada
CP-06 — Exportación JSON
Requerimiento: RF-06
Entrada: conversación existente
Resultado esperado: archivo .json generado
CP-07 — Exportación XML
Requerimiento: RF-07
Entrada: conversación existente
Resultado esperado: archivo .xml generado
CP-08 — Cierre de sesión
Requerimiento: RF-08
Entrada: sesión activa
Resultado esperado: sesión cerrada correctamente
CP-09 — Rendimiento
Requerimiento: RNF-01
Validación: tiempo de respuesta < 5s
CP-10 — Seguridad
Requerimiento: RNF-02
Validación: contraseñas encriptadas
CP-11 — Usabilidad
Requerimiento: RNF-03
Validación: usuario completa flujo sin ayuda
CP-12 — Portabilidad
Requerimiento: RNF-04
Validación: funciona en Windows/Linux
CP-13 — Mantenibilidad
Requerimiento: RNF-05
Validación: código con PEP8 y estructura modular