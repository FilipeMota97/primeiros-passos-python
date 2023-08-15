# Calculadora com while
num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o Segundo numero: "))
operacao = input("Digite a operação que deseja realizar: ")

while operacao == "+" :
    resultado = num1 + num2
    print(f"O Resultado é {resultado}")
    break
while operacao == "-" :
    resultado = num1 - num2
    print(f"O Resultado é {resultado}")
    break
while operacao == "*" :
    resultado = num1 * num2
    print(f"O Resultado é {resultado}")
    break
while operacao == "/" :
    resultado = num1 / num2
    print(f"O Resultado é {resultado}")
    break

   