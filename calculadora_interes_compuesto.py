print("Calculadora de Interes Compuesto")
print("Ejemplo de Uso:Interes 4% -->0.04")
#import matplotlib.pyplot as plt

initial_amount=float(input("Cantidad inicial: "))
interest_rate=float(input("Tasa de interes anual en tantos por uno: "))

print(f"La cantidad inicial a invertir es {initial_amount} a un tipo de interes anual  {interest_rate}")
years=list(range(26))

#year=1
#final_amount = initial_amount * (1 + interest_rate) ** year
#print(final_amount)
#print(initial_amount*interest_rate)
amount=[]
for n in years:
    m=initial_amount * (1 + interest_rate) **n
    m_rounded=round(m,2)
    print(f"resultado final: {m_rounded} en el año : {n}")
    amount.append(m)


"""
plt.title('Compound Interest Grafic')
plt.plot(amount, years)
plt.xlabel('amount')
plt.ylabel('years')
plt.show()
"""
