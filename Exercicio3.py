num = (input("Digite um numero inteiro: "))
try:
    num_int = int(num)
    if num_int % 2 == 0:
         print("O número é par!")
    else:
         print("O número é impar!")
except:
     print("Desculpe, O número digitado não é inteiro")