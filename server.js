const express = require('express');
const path = require('path');
const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, 'js+server')));


function sumar(a, b) {
  return a.map((fila, i) => fila.map((val, j) => val + b[i][j]));
}

function multiplicar(a, b) {
  const filas = a.length;
  const cols  = b[0].length;
  const n     = b.length;
  const res   = Array.from({ length: filas }, () => Array(cols).fill(0));
  for (let i = 0; i < filas; i++)
    for (let j = 0; j < cols; j++)
      for (let k = 0; k < n; k++)
        res[i][j] += a[i][k] * b[k][j];
  return res;
}

app.post('/api/suma', (req, res) => {
  const { matrizA, matrizB } = req.body;

  if (!matrizA || !matrizB)
    return res.status(400).json({ error: 'Faltan las matrices.' });

  if (matrizA.length !== matrizB.length || matrizA[0].length !== matrizB[0].length)
    return res.status(400).json({ error: 'Las matrices deben tener las mismas dimensiones para sumarse.' });

  const resultado = sumar(matrizA, matrizB);
  res.json({ resultado });
});

app.post('/api/multiplicacion', (req, res) => {
  const { matrizA, matrizB } = req.body;

  if (!matrizA || !matrizB)
    return res.status(400).json({ error: 'Faltan las matrices.' });

  const colsA = matrizA[0].length;
  const filasB = matrizB.length;

  if (colsA !== filasB)
    return res.status(400).json({
      error: `Para multiplicar, las columnas de A (${colsA}) deben ser iguales a las filas de B (${filasB}).`
    });

  const resultado = multiplicar(matrizA, matrizB);
  res.json({ resultado });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en http://localhost:${PORT}`);
});
