import operaciones

while True: #Controla si se sigue haciendo el programa principal.
    try:
        num1 = float(input("Introduzca un número: "))
        num2 = float(input("Introduzca otro número: "))
    except ValueError:
        print("No se introdujo un número.")
        continue #Vuelve al principio.
    
    while True: #Segundo bucle. Necesario para cuando se quiera realizar más operaciones con los mismos números.
        print("""Opciones a elegir:
          1) Sumar.
          2) Restar.
          3) Multiplicar.
          4) Dividir.
          5) Salir.""")
    
        try:
            opc = int(input("Introduzca un número de opción: ").strip()) #El .strip() evita los espacios en blanco.
        except ValueError:
            print("No se introdujo un número.")
            continue #Vuelve al principio.
        
        print(" ")
        if opc == 5:
            print("Hasta la próxima. Saliendo........")
            exit() #Finaliza el programa.
        elif opc in [1, 2, 3, 4]:
            
            if opc == 1:
                res = operaciones.suma(num1, num2)
            elif opc == 2:
                res = operaciones.resta(num1, num2)
            elif opc == 3:
                res = operaciones.multi(num1, num2)
            else:
                res = operaciones.divi(num1, num2)
                    
            print(f"El resultado es {res}")
            
            while True: #El tercer bucle sirve para que, si no se pone 's' o 'n', vuelva a preguntar.
                otro = input("¿Deseas realizar otra operación (s/n)? ").strip().lower() 
                #Asegura que acepte una s o una n, independientemente de que esté en mayúscula.
        
                if otro == 's':
                    break #Vuelve al bucle principal.
                elif otro == 'n':
                    print("Hasta la próxima. Saliendo........")
                    exit() #Termina toda ejecución del programa.
                else:
                    print("Opción no válida. Por favor, intoduzca 's' o 'n'.")
        else:
            print("Opción no válida. Por favor introduzca un número del 1 al 5.")