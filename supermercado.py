numero_articulos = int(input("¿Cuántos artículos desea revisar?: "))
alertas_criticas = 0
alertas_medias = 0
suministros_ok = 0

for j in range(numero_articulos):
    id_elemento = input("\nReferencia del artículo: ")
    nombre_elemento = input("Descripción del artículo: ")
    piezas_actuales = int(input("Unidades en bodega: "))

    if piezas_actuales < 10:
        print("Aviso: Nivel crítico. Solicitar pedido urgente.")
        alertas_criticas += 1
    elif 10 <= piezas_actuales <= 50:
        print("Aviso: Nivel bajo. Prestar atención.")
        alertas_medias += 1
    else:
        print("Aviso: Nivel suficiente. Inventario sano.")
        suministros_ok += 1

print("\nReporte de existencias:")
print(f"Referencias en estado crítico: {alertas_criticas}")
print(f"Referencias con nivel bajo: {alertas_medias}")
print(f"Referencias con nivel suficiente: {suministros_ok}")