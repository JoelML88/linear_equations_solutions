
% Definir la matriz A y el vector b
%A = [2 1 -1; -3 -1 2; -1 1 3];
%b = [1; -1; 2];


A = [5,2,-3; 2,10,-8; 3,8,13];
b = [1; 4; 7];


function x = gauss_seidel(A, b, x0, tol, max_iter)
    n = length(b);
    x = x0;
    iter = 0;
    while iter < max_iter
        x_prev = x;
        for i = 1:n
            sigma = 0;
            for j = 1:n
                if j != i
                    sigma += A(i, j) * x(j);
                end
            end
            x(i) = (b(i) - sigma) / A(i, i);
        end
        if norm(x - x_prev, inf) < tol
          disp("Iteraciones:");
          disp(iter+1);
            break;
        end
        iter += 1;
    end
end

% Suposición inicial para x
x0 = zeros(size(b));

% Definir la tolerancia y el número máximo de iteraciones
tolerancia = 0.000000001;
max_iteraciones = 1000;

% Iniciar el cronómetro
tic;

% Resolver el sistema usando Gauss-Seidel
solucion = gauss_seidel(A, b, x0, tolerancia, max_iteraciones);

% Detener el cronómetro y mostrar el tiempo transcurrido
tiempo_transcurrido = toc;
disp(["Tiempo de ejecución:", num2str(tiempo_transcurrido), " segundos"]);


% Mostrar la solución
disp("La solución es:");
disp(solucion);

