efectivo_cuenta = float(input("Ingrese el saldo base de la cuenta: "))

while True:
    print("\n--- Menú de Operaciones ---")
    print("1) Ver fondos disponibles")
    print("2) Sacar dinero")
    print("3) Ingresar dinero")
    print("4) Finalizar")
    
    alternativa = input("Seleccione una opción (1-4): ")

    if alternativa == '1':
        print(f"Su saldo actual es: {efectivo_cuenta:.2f}")
        
    elif alternativa == '2':
        cantidad_retiro = float(input("¿Cuánto dinero desea sacar?: "))
        if cantidad_retiro <= efectivo_cuenta:
            efectivo_cuenta -= cantidad_retiro
            print("Retiro procesado correctamente.")
        else:
            print("Error: No cuenta con fondos suficientes para este retiro.")
            
    elif alternativa == '3':
        cantidad_abono = float(input("¿Cuánto dinero desea ingresar?: "))
        if cantidad_abono > 0:
            efectivo_cuenta += cantidad_abono
            print("Dinero ingresado correctamente.")
        else:
            print("Error: El monto a ingresar debe ser mayor a cero.")
            
    elif alternativa == '4':
        print(f"Operación finalizada. Su saldo final es: {efectivo_cuenta:.2f}")
        break
        
    else:
        print("Opción no válida. Por favor, intente de nuevo.")