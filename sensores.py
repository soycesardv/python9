total_equipos = int(input("Ingrese la cantidad de dispositivos térmicos: "))
zonas_frias = 0
zonas_templadas = 0
zonas_calidas = 0

for i in range(total_equipos):
    medicion_grados = float(input(f"Grados detectados en el dispositivo {i + 1}: "))
    
    if medicion_grados < 18:
        print("Estado: Ambiente frío. Activando calefactores.")
        zonas_frias += 1
    elif 18 <= medicion_grados <= 25:
        print("Estado: Ambiente óptimo. Sin alteraciones.")
        zonas_templadas += 1
    else:
        print("Estado: Ambiente caluroso. Encendiendo refrigeración.")
        zonas_calidas += 1

print("\nResumen de ambientes:")
print(f"Áreas con frío: {zonas_frias}")
print(f"Áreas estables: {zonas_templadas}")
print(f"Áreas con calor: {zonas_calidas}")