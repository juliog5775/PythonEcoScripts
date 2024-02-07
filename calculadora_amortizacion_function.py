def calcu_amort(valor_inicial,años_estimados):
    am_anual=round(valor_inicial/años_estimados,2)
    am_m=round(am_anual/12,2)
    return f"la amortizacion mesual debe ser de {am_m} que en su conjunto sumará una amortizacion anual de {am_anual}"

#Ejemplo de uso: valor inicial 5000 u.m  y vida util estimada en 7 años
resultado=calcu_amort(5000,7)
print(resultado)
    