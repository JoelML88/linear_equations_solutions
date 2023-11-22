

function [x,y] = jacobi(A, b, x0, tol, max_iter)

  disp("************JACOBI***********");
    n = length(b);
    x = x0;
    iter = 0;
    while iter < max_iter
        x_prev = x;
        for i = 1:n
            sigma = 0;
            for j = 1:n
                if j != i
                    sigma += A(i, j) * x_prev(j);
                end
            end
            x(i) = (b(i) - sigma) / A(i, i);
        end
        if norm(x - x_prev, inf) < tol
          disp("Iteraciones:");
          disp(iter+1);
          y=iter+1
            break;
        end
        iter += 1;
    end
    y=iter+1
    disp("************END-JACOBI***********");
end

