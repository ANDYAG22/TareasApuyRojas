# funcion que realiza operaciones matematicas entre dos numeros enteros
def operation_selector(num1, num2, op): 
    if not ((isinstance(num1, int)) & (not isinstance(num1, bool))): # Verifica si el primer numero no es un numero entero ni tampoco una variable booleana para retornar un error
        return -50, None 
    if not ((isinstance(num2, int)) & (not isinstance(num2, bool))): # Verifica si el segundo numero no es un numero entero ni tampoco una variable booleana para retornar un error
        return -50, None
    if not (isinstance(op, str)): # Verifica si el operando no es una variable tipo string para retornar un error
        return -60, None
    
    if (op == '+'): # Verifica si el operando presenta el simbolo de suma para realizar dicha operacion entre los dos numeros y retorna el resultado
        resultado = num1 + num2
        return 0, resultado
    elif (op == '-'): # Verifica si el operando presenta el simbolo de resta para realizar dicha operacion entre los dos numeros y retorna el resultado
        resultado = num1 - num2
        return 0, resultado
    elif (op == '*'): # Verifica si el operando presenta el simbolo de multiplicacion para realizar dicha operacion entre los dos numeros y retorna el resultado
        resultado = num1 * num2
        return 0, resultado
    elif (op == '&'): # Verifica si el operando presenta el simbolo del and para realizar dicha operacion entre los dos numeros y retorna el resultado
        resultado = num1 & num2
        return 0, resultado
    else:
        return -70, None # En caso de que la variable op no cumpla con alguna de las condiciones anteriores se retorna un error


def calculo_promedio(lista_valores):
    # Verificar que todos los elementos en la lista sean números
    for valor in lista_valores:
        if not isinstance(valor, (int, float)) & (not isinstance(valor, bool)):
            return -80, None
    # Verificar que el tamaño de la lista no sea mayor a 10 elementos
    if len(lista_valores) > 10:
        return -90, None
    promedio = sum(lista_valores) / len(lista_valores)
    return 0, promedio
