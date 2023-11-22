import os

def save_file(filename, data):
    if not os.path.isfile(filename):
        with open(filename, 'w') as file:
            file.write("hora_test,algoritmo, tolerancia, max_iteraciones, tiempo_transcurrido,solucion\n")
        print(f"Archivo '{filename}' creado exitosamente.")
    else:
        print(f"El archivo '{filename}' ya existe.")

    with open(filename, 'a') as file:
        file.write(data)
    print("Información agregada al archivo.")
