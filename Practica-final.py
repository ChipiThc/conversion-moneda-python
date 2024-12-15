#1. Definir el valor actual del euro y dolar con respecto al peso mexicano

tipo_cambio_eur_a_mex = 23.70
tipo_cambio_usd_a_mex = 20.75

#2. Solicitar al usuario el tipo de consersion ( euro a mex o dolar a mex)

tipo_conversion = input("Ingrese la moneda de origen para la conversion (EUR/USD):")

#3. Solicitar al usuario el monto a convertir 

monto_a_convertir = float(input("Ingrese el monto a convertir: "))

#4. Realizar la conversion utilizando el tipo de cambio correspondiente
#5. Mostrar el resultado de la conversion al usuario

if tipo_conversion.upper() == "EUR":   
    resultado = monto_a_convertir  + tipo_cambio_eur_a_mex
    print("El resultado de la conversion de EUR a MXN es:", resultado)
elif tipo_conversion.upper() == "USD":
    resultado = monto_a_convertir * tipo_cambio_usd_a_mex
    print("El resultado de la conversion de EUR a MXN es:", resultado)
else:
    print("No esta disponible este tipo de conversion actualmente")