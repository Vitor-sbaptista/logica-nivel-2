'''
21) A jornada de trabalho semanal de um funcionário é de 40 horas.
O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo
é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que 
leia o número de horas trabalhadas em um mês, o salário por hora e escreva o
salário total do funcionário, que deverá ser acrescido das horas extras, caso
tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).
'''
horas_trabalhadas = float(input("Digite o número total de horas trabalhadas no mês: "))
salario_por_hora = float(input("Digite o valor do sálario por hora: "))

horas_normais_mensais = 40 * 4

if horas_trabalhadas > horas_normais_mensais:
    horas_extras = horas_trabalhadas - horas_normais_mensais
    salario_base = horas_normais_mensais * salario_por_hora
    salario_extra = horas_extras * salario_por_hora * 1.5
    salario_total = salario_base + salario_extra
else:
    salario_total = horas_trabalhadas * salario_por_hora
    
print(f"O salário total do funcionário é: R${salario_total}.")
