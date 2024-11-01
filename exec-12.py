'''
12) Faça um algoritmo que leia três notas de um aluno, calcule e escreva a 
média final deste aluno. Considerarque a média é ponderada e que o peso das 
notas é 2, 3 e 5. Fórmula para o cálculo da média final é:
'''
nota1 = float(input("Qual a primeira nota? "))
nota2 = float(input("Qual a segunda nota? "))
nota3 = float(input("Qual a terceira nota? "))

media_final = ((nota1*2) + (nota2*3) + (nota3*5)) / 10

print("A média final é: ", media_final)
