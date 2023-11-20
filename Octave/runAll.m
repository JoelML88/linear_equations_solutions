A = [2 -1 1; 1 3 -1; 1 1 4];
b = [3; 7; 4];

% Suposición inicial para x
x0 = zeros(size(b));


% Definir la tolerancia y el número máximo de iteraciones
tolerancia = 0.000000001;
max_iteraciones = 1000;

% Iniciar el cronómetro
tic;
  solucion = jacobi(A, b, x0, tolerancia, max_iteraciones);
  disp("La solución JACOBI:");
  disp(solucion);
% Detener el cronómetro y mostrar el tiempo transcurrido
tiempo_transcurrido = toc;
disp(["Tiempo de ejecución:", num2str(tiempo_transcurrido), " segundos"]);





% Iniciar el cronómetro
tic;

% Resolver el sistema usando Gauss-Seidel
solucion = gauss_seidel(A, b, x0, tolerancia, max_iteraciones);

% Detener el cronómetro y mostrar el tiempo transcurrido
tiempo_transcurrido = toc;
disp(["Tiempo de ejecución:", num2str(tiempo_transcurrido), " segundos"]);


% Mostrar la solución
disp("La solución de GAUSS-SEIDEL:");
disp(solucion);


omega = 1.2;
% Iniciar el cronómetro
tic;
solucion = sor(A, b, x0, omega, tolerancia, max_iteraciones);
% Detener el cronómetro y mostrar el tiempo transcurrido
tiempo_transcurrido = toc;
disp("La solución SOR:");
disp(solucion);

