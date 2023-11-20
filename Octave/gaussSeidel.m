

function x = gaussSeidel(A, b, x0, tol, max_iter)

  disp("************GAUSS-SEIDEL***********");
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
    disp("************END-GAUSS-SEIDEL***********");
end



