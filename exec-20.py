'''
20) Ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas
horas inteiras, sem os minutos) e calcule a duração do jogo em horas, 
sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo
pode iniciar em um dia e terminar no dia seguinte.
'''
hora_inicio = int(input("Que horas a partida começou? "))
hora_fim = int(input("Que horas a partida terminou? "))

if hora_fim > hora_inicio:
    duracao = hora_fim - hora_inicio
else:
    duracao = (24 - hora_inicio) + hora_fim

print(f"A duração do jogo foi de {duracao} horas.")
