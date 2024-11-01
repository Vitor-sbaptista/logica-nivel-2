'''
11) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular
e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):
'''
temperaturaF = float(input("Qual a temperatura em Fahrenheit? "))

celcius = (temperaturaF-32) * 5/9
print("Valor em celcius é: ", celcius)
