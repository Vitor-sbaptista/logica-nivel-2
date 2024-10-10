3) Os pares de instruções abaixo produzem o mesmo resultado? Imprima os valores abaixo, veja se algum deles (A, B ou C) possuem valores diferentes nas versões 1 e 2, e caso sim, explique num comentário o motivo.

A1 ← (4/2)+(2/4)	e	A2 ← 4/2+2/4
B1 ← 4/(2+2)/4	e	B2 ← 4/2+2/4
C1 ← (4+2)*2-4	e	C2 ← 4+2*2-4


A1 = (4/2)+(2/4)
A2 = 4/2+2/4

print("O valor de A1 é ", A1)
print("O valor de A2 é ", A2)

B1 = 4/(2+2)/4
B2 = 4/2+2/4

print("O valor de B1 é ", B1)
print("O valor de B2 é ", B2)

C1 = (4+2)*2-4
C2 = 4+2*2-4

print("O valor de C1 é ", C1)
print("O valor de C2 é ", C2)
