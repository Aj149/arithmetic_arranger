def mostrar_problemas_aritmeticos(problemas, mostrar_respuestas=False):
    # Verificar el número máximo de problemas permitidos
    if len(problemas) > 5:
        return "Error: Too many problems."

    # Inicializar listas para almacenar los operandos y operadores
    operandos = []
    operadores = []

    # Verificar y dividir los problemas en operandos y operadores
    for problema in problemas:
        partes = problema.split()
        if len(partes) != 3:
            return "Error: Each problem should have two operands and one operator."
        operandos.append((partes[0], partes[2]))
        operadores.append(partes[1])

    # Verificar operadores válidos
    if any(operador not in ['+', '-'] for operador in operadores):
        return "Error: Operator must be '+' or '-'."

    # Verificar dígitos válidos en operandos
    if any(not operando.isdigit() for par in operandos for operando in par):
        return "Error: Numbers must only contain digits."

    # Verificar longitud máxima de operandos
    if any(len(operando) > 4 for par in operandos for operando in par):
        return "Error: Numbers cannot be more than four digits."

    # Preparar los problemas para mostrar
    lineas = []
    respuestas = []

    for i, (operandos, operador) in enumerate(zip(operandos, operadores)):
        num1, num2 = operandos

        # Realizar la operación y obtener la respuesta si es necesario
        if mostrar_respuestas:
            if operador == '+':
                respuesta = int(num1) + int(num2)
            else:
                respuesta = int(num1) - int(num2)
            respuestas.append(respuesta)

        # Construir la línea del problema
        linea = num1.rjust(len(num2) + 2)
        linea += '\n' + operador + ' ' + num2.rjust(len(num1))
        linea += '\n' + '-' * (len(linea.splitlines()[0]))

        lineas.append(linea)

    # Concatenar los problemas y las respuestas si es necesario
    resultado = '\n'.join(lineas)
    if mostrar_respuestas:
        respuestas_str = '    '.join(map(str, respuestas))
        resultado += '\n\nRespuestas:\n' + respuestas_str

    return resultado

problemas = ["32 + 5", "4 - 12", "123 + 4567", "888 + 222", "45 - 23"]
print(mostrar_problemas_aritmeticos(problemas, mostrar_respuestas=True))
