salario=float(input("Por favor informe o seu salário:"))
if salario<128.000:
     percentagem=0.2
     aumento=salario*percentagem
     novo_salario=salario+aumento
elif salario>=128.000 or salario<=500.000:
     percentagem=0.15
     aumento=salario*percentagem
     novo_salario=salario+aumento
elif salario>=500.00 or salario<=1.000000:
     percentagem=0.1
     aumento=salario*percentagem
     novo_salario=salario+aumento
else:
    percentagem=0.05
    aumento=salario*percentagem
    novo_salario=salario+aumento

print(" Salário antes do reajustes é:",salario,"00")
print(" A Percentagem é de:" ,percentagem,"00")
print(" Aumento a ser aplicado é:",novo_salario,"00")
        
         
