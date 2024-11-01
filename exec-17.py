'''
17) Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem
que diga se ela poderá ou não votar este ano (não é necessário considerar o 
mês em que a pessoa nasceu).
'''
ano_atual = int(input("Em que ano estamos? "))
ano_nascimento = int(input("Em qual ano você nasceu? "))

if ano_nascimento<=2006:
    print("Pode votar.")
else:
    print("Não pode votar.")
