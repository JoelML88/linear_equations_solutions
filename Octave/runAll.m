
%{

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

% Tamaño de la matriz y del vector
n = 50;

% Generar una matriz aleatoria
A = rand(n, n);

% Convertir la matriz en estrictamente diagonal dominante
for i = 1:n
    A(i, i) = sum(abs(A(i, :))) + rand * 10;
end

% Generar un vector aleatorio
b = rand(n, 1);



%}


A = [10,-1,2,0;
    -1,11,-1,3;
     2,-1,10,-1;
     0,3,-1,8]

 b = [6;25;-11;15]








%disp(A);
%disp(b);

% Suposición inicial para x
x0 = zeros(size(b));

% Definir la tolerancia y el número máximo de iteraciones
tolerancia = 0.00001;
max_iteraciones = 10000;

% Iniciar el cronómetro
tic;
  [solucion, it] = jacobi(A, b, x0, tolerancia, max_iteraciones);
  % Detener el cronómetro y mostrar el tiempo transcurrido
  tiempo_transcurrido = toc;

  %Escribimos log
  toPrint = sprintf("%s,Jacobi,%s,%s,%s,%s,%s \n",datestr(clock(), 'yyyy-mm-dd HH:MM:SS'), num2str(tolerancia), num2str(max_iteraciones), num2str(tiempo_transcurrido),num2str(it),sprintf('%d ', solucion));
  archiveName = sprintf("Jacobi_%s.csv",datestr(now, 'dd.mm.yyyy'));
  saveFile(archiveName,toPrint);


  disp(["Tiempo de ejecución JACOBI:", num2str(tiempo_transcurrido), " segundos"]);

  disp("La solución JACOBI:");
  disp(solucion);


x0 = zeros(size(b));
% Iniciar el cronómetro
tic;
% Resolver el sistema usando Gauss-Seidel
[solucion, it] = gaussSeidel(A, b, x0, tolerancia, max_iteraciones);

% Detener el cronómetro y mostrar el tiempo transcurrido
tiempo_transcurrido = toc;

  %Escribimos log
  toPrint = sprintf("%s,Gauss-Seidel,%s,%s,%s,%s,%s \n",datestr(clock(), 'yyyy-mm-dd HH:MM:SS'), num2str(tolerancia), num2str(max_iteraciones), num2str(tiempo_transcurrido),num2str(it),sprintf('%d ', solucion));
  archiveName = sprintf("Gauss-Seidel_%s.csv",datestr(now, 'dd.mm.yyyy'));
  saveFile(archiveName,toPrint);

disp(["Tiempo de ejecución GAUSS:", num2str(tiempo_transcurrido), " segundos"]);
% Mostrar la solución
disp("La solución de GAUSS-SEIDEL:");
disp(solucion);


omega = 1.2;
x0 = zeros(size(b));
% Iniciar el cronómetro
tic;
[solucion, it] = sor(A, b, x0, omega, tolerancia, max_iteraciones);
% Detener el cronómetro y mostrar el tiempo transcurrido
tiempo_transcurrido = toc;

  %Escribimos log
  toPrint = sprintf("%s,SOR,%s,%s,%s,%s,%s \n",datestr(clock(), 'yyyy-mm-dd HH:MM:SS'), num2str(tolerancia), num2str(max_iteraciones), num2str(tiempo_transcurrido),num2str(it),sprintf('%d ', solucion));
  archiveName = sprintf("SOR_%s.csv",datestr(now, 'dd.mm.yyyy'));
  saveFile(archiveName,toPrint);

disp(["Tiempo de ejecución SOR:", num2str(tiempo_transcurrido), " segundos"]);
disp("La solución SOR:");
disp(solucion);

