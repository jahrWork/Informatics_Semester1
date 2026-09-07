# Metodología: Conocimiento Restringido y Antialucinaciones

Esta regla fuerza al agente (Antigravity) a usar un conocimiento estrictamente limitado a los archivos del proyecto.

## 1. Restricción Estricta
- Para responder a CUALQUIER pregunta, debes basarte **ÚNICA Y EXCLUSIVAMENTE** en el contenido de los archivos de este proyecto y en los documentos PDF/texto ubicados en la carpeta `documentos_referencia/`.
- Tienes PROHIBIDO utilizar tu conocimiento general o de internet para responder preguntas técnicas, teóricas o de código que no estén sustentadas en estos documentos.
- Si la respuesta no se encuentra explícitamente en los documentos o en el código, debes responder exactamente con la frase: **"No se encuentra en los documentos"**.

## 2. Escaneo Automático de Documentos
- Cada vez que el usuario te haga una pregunta, debes usar la herramienta `list_dir` para revisar el contenido de la carpeta `documentos_referencia/` (si existe).
- Debes leer los PDFs (con `view_file`) de esa carpeta que consideres relevantes para la pregunta antes de emitir cualquier respuesta.

## 3. Estándares de Código
- **Comentarios:** Todo el código que escribamos debe llevar comentarios explicativos en inglés.
- **Nomenclatura:** Se debe usar siempre el estilo `snake_case` para el nombre de las variables y funciones.
- **Tests Unitarios:** Siempre se deben crear tests unitarios para validar las nuevas funciones que se implementen.
