nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
if nome != None and idade != None:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    if " " in nome:
        print("Seu nome contem espaços!")
    else: 
        print("Seu nome nao contem espaços!")
    print(f"Seu nome contem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")

else:
    print("Desculpe, você deixou campos vazios!")