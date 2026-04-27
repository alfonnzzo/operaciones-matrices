# Operaciones con Matrices

## ¿Qué hace la app?

* Podés elegir el tamaño de las matrices (desde 1x1 hasta 6x6).
* Valida que ingreses números correctamente (te marca los errores en rojo antes de operar).
* Calcula suma o multiplicación y te muestra el resultado en la misma página.
* Para multiplicar, valida automáticamente la regla matemática: *las columnas de la matriz A tienen que ser iguales a las filas de la matriz B*.

---

## ¿Cómo levantar cada versión?

> **Aviso importante:** Dejá los archivos `server.js` y `app.py` en la raíz del proyecto. Si los metés adentro de las carpetas, los servidores no van a encontrar el HTML.

### 1. Solo Cliente (`no-server/`)
La más fácil, todo se calcula en el navegador con JavaScript. No necesitás instalar nada.
* Entrá a la carpeta `no-server` y hacé doble clic en el `index.html` para abrirlo en tu navegador.

### 2. Backend Node.js (`js+server/`)
La lógica de cálculo se hace en un servidor con Express.
1. Desde la raíz del proyecto, abrí la terminal.
2. Ejecutá:
   ```bash
   npm install
   node server.js
   ```
3. Abrí tu navegador en **http://localhost:3000**

### 3. Backend Python (`py+server/`)
Misma idea que la versión anterior, pero el servidor está hecho con Flask.
1. Desde la raíz del proyecto, abrí la terminal.
2. Ejecutá:
   ```bash
   pip install flask
   python app.py
   ```
3. Abrí tu navegador en **http://localhost:5000** 

---

## Resumen Técnico

| Versión | Stack / Tecnologías | Arranque |
|---|---|---|
| **Frontend Puro** | HTML, CSS, JS (ES6+) | Doble clic al archivo `index.html` |
| **Node.js** | Node, Express.js | `node server.js` |
| **Python** | Python (3.8+), Flask | `python app.py` |
