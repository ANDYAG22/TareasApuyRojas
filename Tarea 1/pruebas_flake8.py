# Funcion que muestra holaMundo cuando variable=14
def holaMundo():
    variable = 14
    if (variable == 14):  # Verifica si variable es igual a 14
        print("Hola Mundo")  # Imprime en terminal "hola mundo"
    else:
        # Imprime en terminal el valor que debe tener variable
        print("La variable es: ", variable, " pero debe ser un valor de 14")


holaMundo()
