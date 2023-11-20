A = [4, -1, 0, -1, 0, 0, 0, 0, 0;
    -1, 4, -1, 0, -1, 0, 0, 0, 0;
    0, -1, 4, 0, 0, -1, 0, 0, 0;
    -1, 0, 0, 4, -1, 0, -1, 0, 0;
    0, -1, 0, -1, 4, -1, 0, -1, 0;
    0, 0, -1, 0, -1, 4, 0, 0, -1;
    0, 0, 0, -1, 0, 0, 4, -1, 0;
    0, 0, 0, 0, -1, 0, -1, 4, -1;
    0, 0, 0, 0, 0, -1, 0, -1, 4];

b = [150; 100; 150; 50; 0; 50; 50; 0; 50];

% Suposición inicial para x
x0 = zeros(size(b));


% Definir la tolerancia y el número máximo de iteraciones
tolerancia = 0.000000001;
max_iteraciones = 1000;

% Iniciar el cronómetro
tic;
  solucion = jacobi(A, b, x0, tolerancia, max_iteraciones);
  % Detener el cronómetro y mostrar el tiempo transcurrido
  tiempo_transcurrido = toc;
  disp(["Tiempo de ejecución JACOBI:", num2str(tiempo_transcurrido), " segundos"]);

  disp("La solución JACOBI:");
  disp(solucion);


x0 = zeros(size(b));
% Iniciar el cronómetro
tic;
% Resolver el sistema usando Gauss-Seidel
solucion = gaussSeidel(A, b, x0, tolerancia, max_iteraciones);

% Detener el cronómetro y mostrar el tiempo transcurrido
tiempo_transcurrido = toc;
disp(["Tiempo de ejecución GAUSS:", num2str(tiempo_transcurrido), " segundos"]);


% Mostrar la solución
disp("La solución de GAUSS-SEIDEL:");
disp(solucion);


omega = 1.2;
x0 = zeros(size(b));
% Iniciar el cronómetro
tic;
solucion = sor(A, b, x0, omega, tolerancia, max_iteraciones);
% Detener el cronómetro y mostrar el tiempo transcurrido
tiempo_transcurrido = toc;
disp(["Tiempo de ejecución SOR:", num2str(tiempo_transcurrido), " segundos"]);


disp("La solución SOR:");
disp(solucion);

