nome = input("Digite seu nome: ")
altura = eval(input("Digite sua altura: "))
peso = eval(input("Digite seu peso: "))
imc = peso/(altura**2)
print(f"O IMC de {nome} é igual a {imc:.2f} ")