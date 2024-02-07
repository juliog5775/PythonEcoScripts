print("Calculadora de amortización por el metodo lineal")

valor_inicial=float(input("Introduce el valor inicial del moviliario a amortizar: "))

vida_util=int(input("Introduce la vida util estimada en años: "))

amortizacion_anual=valor_inicial/vida_util
print(f"la amortización anual debe ser de {round(amortizacion_anual,2)} unidades monetarias por año")
print(f"la amortización mensual debe ser de {round(amortizacion_anual/12,2)} unidades monetarias ")

for i in range(vida_util+1):
    if i==0:
        valor_actual=valor_inicial
    else:
        valor_actual=valor_inicial-amortizacion_anual
        valor_inicial=valor_actual
    print(f"El valor actual en el año {i} será de {valor_actual} u.m")
    i+1
    