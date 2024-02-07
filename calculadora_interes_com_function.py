#calculadora del tipo de interes compuesto 
def calculadora_interes(initial_amount,interest_rate,years):
    years=range(years+1)
    for i in years:
         m=initial_amount * (1 +interest_rate) **i
         m_rounded=round(m,2)
    return m_rounded

##ejemplo de uso con cantidad inicial =10000 , tipo de interes= 5% , años =25
resultado=calculadora_interes(1000,0.05,25)
print(resultado)