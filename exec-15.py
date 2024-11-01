'''
15) As maçãs custam R$ 1,30 cada se forem compradas menos de uma 
dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que 
leia o número de maçãs compradas, calcule e escreva o custo total da compra.
'''
fruta = float(1.30)
frutaPromocao = int(1)

x = int(input("Quantas frutas foram compradas? "))

if x>=12:
    print("O total foi de R$", x*frutaPromocao)
else:
    print("O total foi de R$", x*fruta)
