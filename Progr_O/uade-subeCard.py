# Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo
# dentro de un mes. Sabiendo que dicho medio de transporte utiliza un esquema
# de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarrollar
# una función que reciba como parámetro la cantidad de viajes realizados en un
# determinado mes y devuelva el total gastado en viajes. Realizar también un programa
# para verificar el comportamiento de la función.
# Cantidad de viajes  Valor del pasaje
#12.50$  1 a 20              Averiguar valor actualizado
#20% 21 a 30             20% de descuento sobre tarifa máxima
#30% dif 31 a 40             30% de descuento sobre tarifa máxima
#40% Más de 40           40% de descuento sobre tarifa máxima
#Tener en cuenta uqe se debe cobrar tarifa por cada cant viajes
#Ejemplo 45 viajes:

# Viajes de  1 a 20: 12.50 * 20 = 250
# Viajes de 21 a 30: 10.00 * 10 = 100
# Viajes de 31 a 40:  8.75 * 10 = 87.50
# Viajes mayor a 41:  7.50 *  5 = 37.50
# Importe total: 475$

def subeCard(cantViajes, tarifaOrig=12.50):
    priceToPay = 0
    for i in range(1,cantViajes+1):
        if i <= 20:
            tarifa = tarifaOrig
        elif 21 <= i <= 30:
            tarifa = tarifaOrig - tarifaOrig*0.20
        elif 31 <= i <= 40:
            tarifa = tarifaOrig - tarifaOrig*0.30
        elif i > 40:
            tarifa = tarifaOrig - tarifaOrig*0.40

        priceToPay += tarifa

    return priceToPay

print("----------------------")
print(subeCard((input("- cant viaejs pls: "))))
print("----------------------")
