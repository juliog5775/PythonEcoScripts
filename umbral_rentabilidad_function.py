def umbral_rentabilidad(precio_unidad,coste_variable_unidad,coste_fijo_total):
    margen_contribucion=precio_unidad-coste_variable_unidad
    punto_muerto=coste_fijo_total/margen_contribucion
    return round(punto_muerto,2)


#ejemplo de uso con un precio de 10 u.m, coste variable unitario  de 7 u.m y coste total fijo  de 5000 u.m
print(umbral_rentabilidad(10,7,5000))
    