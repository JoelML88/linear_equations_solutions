function jacobi(A, b, x0, tol, maxIter) {
    const n = A.length;
    let x = x0.slice(); // Copia inicial de x0

    

    for (let iter = 0; iter < maxIter; iter++) {
        let x_prev = x.slice(); // Copia de la iteración anterior de x

        for (let i = 0; i < n; i++) {
            let sigma = 0;
            for (let j = 0; j < n; j++) {
                if (j !== i) {
                    sigma += A[i][j] * x_prev[j];
                }
            }
            x[i] = (b[i] - sigma) / A[i][i];
        }

        // Calcular la norma para verificar la convergencia
        let norm = 0;
        for (let i = 0; i < n; i++) {
            norm += Math.abs(x[i] - x_prev[i]);
        }

        if (norm < tol) {
            console.log(`Convergió en ${iter + 1} iteraciones.`);
            console.log(x)
            return {solution: x, iterations: iter + 1};
        }
    }

    console.log(`Se alcanzó el máximo de iteraciones (${maxIter}).`);
    console.log(x)
    return {solution: x, iterations: iter + 1};
}

module.exports = jacobi; // Exportar la función para poder importarla en otro archivo