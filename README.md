
# 📌UML + Python

Este proyecto integra diagramas UML con código Python funcional para un sistema de reservas, aplicando buenas prácticas de diseño, control de versiones y colaboración en equipo.
---

## 🔄 Flujo de trabajo recomendado

1. Diseñar el diagrama UML en PlantUML (`.puml`).
2. Escribir o actualizar el código Python.
3. Probar el funcionamiento desde la consola.
4. Si hay cambios de lógica, actualizar el diagrama UML.
5. Confirmar los cambios con `git add` y `git commit`.

---

## ✅ Buenas prácticas en equipo

- Cada cambio en el código debe reflejarse en el UML.
- Usar mensajes de commit claros:
  - `feat: añadida clase Usuario`
  - `refactor: actualizado reserva.puml`
- Mantener las imágenes UML generadas para facilitar revisiones.

---

## ✏️ Simulación de cambio

- Se añadió el atributo `estado: str` a la clase `Reserva`.
- Se actualizó el UML (`reserva.puml`) y su imagen (`reserva.png`).
- Commit correspondiente:
  ```
  git commit -m "feat: agregado atributo estado a Reserva y actualizado UML"
  ```

---

## 🛠 Herramientas utilizadas

- Visual Studio Code + PlantUML
- Python
- Git para control de versiones

---

## 👤 Rol

Me encargué del diseño de clases, implementación en Python, sincronización con UML y documentación del proyecto.
