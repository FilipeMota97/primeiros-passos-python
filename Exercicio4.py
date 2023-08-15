# Exercicio para calcular data e hora e dar um Bom dia, Boa Tarde ou Boa Noite
horas = int(input("Digite a Hora atual: "))
hora_minutos = horas*60
minutos = int(input("Digite os minutos atuais: "))
minutos_totais = hora_minutos + minutos
if minutos_totais >=0 and minutos_totais<=660:
    print(f"Bom dia, São exatamente {horas}:{minutos} da Manhã ")
elif minutos_totais >660 and minutos_totais<=1020:    
    print(f"Boa Tarde, São exatamente {horas}:{minutos} da Tarde ")
elif minutos_totais>1020 and minutos_totais<1440:
    print(f"Boa noite, São exatamente {horas}:{minutos} da Noite ")    
else:
    print("Você digitou uma hora desconhecida!")

