# Suma y Multiplicación de Matrices

Proyecto con tres implementaciones de una aplicación web para operar con matrices: una versión puramente cliente y dos versiones cliente-servidor (Node.js y Python).

---

## Estructura del proyecto

```
proyecto/
├── README.md
├── server.js                   # Backend Node.js (Express)
├── package.json
├── package-lock.json
├── app.py                      # Backend Python (Flask)
├── node_modules/
├── js+server/
│   └── index.html              # Frontend servido por Node.js
├── py+server/
│   └── index.html              # Frontend servido por Python
└── no-server/
    └── index.html              # App completa sin servidor
```

> **Importante:** `server.js` y `app.py` deben estar en la raíz del proyecto, al mismo nivel que las carpetas `js+server/`, `py+server/` y `no-server/`. Si se mueven a otra ubicación, los servidores no van a encontrar los archivos HTML.

---

## Funcionalidades

Todas las versiones comparten las mismas funcionalidades:

- El usuario define la cantidad de filas y columnas (entre 1 y 6)
- Se generan dinámicamente las grillas de las dos matrices
- Se valida que todos los campos estén completos y sean numéricos antes de operar
- Las celdas inválidas se marcan visualmente en rojo
- Se puede elegir entre **suma** y **multiplicación**
- Para la multiplicación se valida que las dimensiones sean compatibles (columnas de A = filas de B)
- La matriz resultado se muestra en la misma página

---

## Versión 1 — Solo cliente (`no-server/`)

El cálculo se realiza directamente en el navegador con JavaScript puro. No requiere servidor ni instalación.

### Requisitos

- Cualquier navegador moderno

### Cómo usar

Abrí el archivo directamente en el navegador haciendo doble clic, o arrastrándolo:

```
no-server/index.html
```

No se necesita ningún servidor ni comando adicional.

---

## Versión 2 — Cliente + Node.js (`js+server/`)

El frontend envía las matrices al servidor vía `fetch` (API REST). El servidor Express realiza el cálculo y devuelve el resultado en JSON.

El archivo `js+server/index.html` **no debe abrirse directamente** con doble clic. Siempre se accede a través del servidor en `http://localhost:3000`.

### Requisitos

- [Node.js](https://nodejs.org/) v18 o superior

### Cómo ejecutar

Desde la raíz del proyecto (donde está `server.js`):

```bash
npm install
node server.js
```

Luego abrí el navegador en: **http://localhost:3000**

### Estructura de la API

| Método | Endpoint               | Descripción               |
|--------|------------------------|---------------------------|
| POST   | `/api/suma`            | Suma dos matrices         |
| POST   | `/api/multiplicacion`  | Multiplica dos matrices   |

**Body esperado (JSON):**
```json
{
  "matrizA": [[1, 2], [3, 4]],
  "matrizB": [[5, 6], [7, 8]]
}
```

**Respuesta exitosa:**
```json
{
  "resultado": [[6, 8], [10, 12]]
}
```

---

## Versión 3 — Cliente + Python (`py+server/`)

Misma lógica que la versión Node.js pero con un backend en Python usando Flask. El frontend es idéntico; solo cambia el servidor.

El archivo `py+server/index.html` **no debe abrirse directamente** con doble clic. Siempre se accede a través del servidor en `http://localhost:5000`.

### Requisitos

- Python 3.8 o superior
- pip

### Cómo ejecutar

Desde la raíz del proyecto (donde está `app.py`):

```bash
pip install flask
python app.py
```

Luego abrí el navegador en: **http://localhost:5000**

### Estructura de la API

| Método | Endpoint               | Descripción               |
|--------|------------------------|---------------------------|
| POST   | `/api/suma`            | Suma dos matrices         |
| POST   | `/api/multiplicacion`  | Multiplica dos matrices   |

El formato de body y respuesta es idéntico al de la versión Node.js.

---

## Comparación entre versiones

| Característica          | `no-server/`         | `js+server/`            | `py+server/`           |
|-------------------------|----------------------|-------------------------|------------------------|
| Requiere instalación    | No                   | Sí (Node + npm)         | Sí (Python + pip)      |
| Cómo se abre            | Doble clic al HTML   | http://localhost:3000   | http://localhost:5000  |
| Cálculo en              | Navegador            | Servidor                | Servidor               |
| Backend                 | —                    | Express.js              | Flask                  |
| Comando para iniciar    | —                    | `node server.js`        | `python app.py`        |

---

## Notas sobre la multiplicación de matrices

Para que la multiplicación sea posible se debe cumplir:

> **columnas de A = filas de B**

El resultado de multiplicar una matriz de **n×k** por una de **k×m** es una matriz de **n×m**.

En las versiones con servidor, esta validación se realiza tanto en el frontend (para dar feedback inmediato al usuario) como en el backend (como salvaguarda adicional).

---

## Tecnologías utilizadas

- **HTML5 + CSS3 + JavaScript (ES6+)** — frontend de las tres versiones
- **Node.js + Express** — backend versión `js+server`
- **Python + Flask** — backend versión `py+server`
"# operaciones-matrices" 
