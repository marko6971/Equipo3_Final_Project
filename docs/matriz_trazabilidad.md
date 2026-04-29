# Matriz de Trazabilidad

| ID Req | Tipo | Caso de Uso | Módulo (futuro) | Caso de Prueba |
|--------|------|------------|-----------------|---------------|
| RF-01 | Funcional | Iniciar sesión | auth.py | CP-01 |
| RF-02 | Funcional | Cargar archivo | file_loader.py | CP-02 |
| RF-03 | Funcional | Enviar pregunta | chat_ui.py / ia_service.py | CP-03 |
| RF-04 | Funcional | Guardar conversación | database.py | CP-04 |
| RF-05 | Funcional | Consultar historial | history.py | CP-05 |
| RF-06 | Funcional | Exportar JSON | exporter.py | CP-06 |
| RF-07 | Funcional | Exportar XML | exporter.py | CP-07 |
| RF-08 | Funcional | Cerrar sesión | auth.py | CP-08 |
| RNF-01 | No funcional | Rendimiento | sistema general | CP-09 |
| RNF-02 | No funcional | Seguridad | auth.py / database.py | CP-10 |
| RNF-03 | No funcional | Usabilidad | UI | CP-11 |
| RNF-04 | No funcional | Portabilidad | sistema general | CP-12 |
| RNF-05 | No funcional | Mantenibilidad | estructura proyecto | CP-13 |