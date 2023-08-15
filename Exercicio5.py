nome = input("Digite seu nome: ")
tamanho_nome = len(nome)


if nome.isdigit():
     print("Nome não pode conter números")
else:    
    if tamanho_nome <=1:
            print("Digite um nome com no mínimo dois caracteres")
    elif tamanho_nome > 1 and tamanho_nome <=4:
            print(f"Olá {nome}, Seu nome é curto")
    elif tamanho_nome > 5 and tamanho_nome <=6:
            print(f"Olá {nome}, Seu nome é normal")
    else:
            print(f"Olá {nome}, seu nome é muito grande")