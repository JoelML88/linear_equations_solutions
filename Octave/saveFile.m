function saveFile(filename, data)

      if exist(filename, 'file') == 0
        fid = fopen(filename, 'w');
        if fid == -1
            error(sprintf("No se pudo crear el archivo '%s'.", filename));
        else
            fprintf(fid, "hora_test,algoritmo, tolerancia, max_iteraciones, tiempo_transcurrido,solucion\n");
            fclose(fid);
            disp(sprintf("Archivo '%s' creado exitosamente.", filename));
        end
    else
        disp(sprintf("El archivo '%s' ya existe.", filename));
    end



    fid = fopen(filename, 'a');  % Abre el archivo en modo de agregar ('a')
    if fid == -1
        error("No se pudo abrir o crear el archivo.");
    else
        fputs(fid, data);  % Agrega la información al archivo
        fclose(fid);  % Cierra el archivo
        disp("Información agregada al archivo.");
    end
end
