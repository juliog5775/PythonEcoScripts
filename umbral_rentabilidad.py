print("Programa para obtener el Umbral de rentabilidad")
print("El umbral de rentabilidad es una medida que nos permite saber a partir de que volumen de ventas se empieza a obtener beneficios")

precio_unidad=float(input("Introduce el precio final por unidad: "))
coste_variable_unitario=float(input("Introduce el coste variable unitario por unidad: "))
costes_fijos=float(input("Introduce los costes fijos totales: "))


print("El margen de contribución unitario es la cantidad de dinero que cada unidad vendida aporta para pagar los costes fijos.")
margen_contribucion_unitario=precio_unidad - coste_variable_unitario

print(f"En este caso el margen de contribución es {margen_contribucion_unitario} u.m por unidad")

umbral_rentabilidad= round(costes_fijos/margen_contribucion_unitario,2)
print(f" A partir de {umbral_rentabilidad} unidades vendidas la empresa empieza a obtener beneficios")