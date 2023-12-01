const jacobi = require('./jacobi'); // Importar la función jacobi desde el archivo jacobi.js

const fs = require('fs');
const { performance } = require('perf_hooks');

function generateRandomMatrix(n) {
    const matrix = [];
    for (let i = 0; i < n; i++) {
        const row = [];
        for (let j = 0; j < n; j++) {
            row.push(Math.random());
        }
        matrix.push(row);
    }
    return matrix;
}

function makeDiagonallyDominant(matrix) {
    const n = matrix.length;
    for (let i = 0; i < n; i++) {
        const absSum = matrix[i].reduce((acc, val) => acc + Math.abs(val), 0);
        matrix[i][i] = absSum + Math.random() * 10;
    }
}

function generateRandomVector(n) {
    const vector = [];
    for (let i = 0; i < n; i++) {
        vector.push(Math.random());
    }
    return vector;
}

function saveFile(filename, data) {
    if (!fs.existsSync(filename)) {
        fs.writeFileSync(filename, "hora_test,algoritmo, tolerancia, max_iteraciones, tiempo_transcurrido,iteraciones,solucion\n");
        console.log(`Archivo '${filename}' creado exitosamente.`);
    } else {
        console.log(`El archivo '${filename}' ya existe.`);
    }

    fs.appendFileSync(filename, data);
    console.log("Información agregada al archivo.");
}



// Tamaño de la matriz y del vector
const n = 5;

// Generar una matriz aleatoria
const A = generateRandomMatrix(n);

// Convertir la matriz en estrictamente diagonal dominante
makeDiagonallyDominant(A);

// Generar un vector aleatorio
const b = generateRandomVector(n);

console.log("\n************MATRIZ A******************");
console.log(A);
console.log("\n************VECTOR B*******************");
console.log(b);

const x0 = new Array(b.length).fill(0);
const tolerance = 0.00001;
const maxIterations = 1000;

console.log("\n*******************************************");
const inicio = performance.now();
const resJacobi = jacobi(A, b, x0, tolerance, maxIterations);

const solution= resJacobi.solution;

const iteraciones = resJacobi.iterations;
const fin = performance.now();

console.log("\n************SOLUCION*******************");
console.log(solution);

// Escribir log
const dataToAdd = `${new Date().toISOString()},Jacobi,${tolerance},${maxIterations},${(fin - inicio)/ 1000},${iteraciones+1},${solution.toString().replace(/\n/g, '')}\n`;
const archiveName = `Jacobi_${new Date().toISOString().split('T')[0]}.csv`;

saveFile(archiveName, dataToAdd);