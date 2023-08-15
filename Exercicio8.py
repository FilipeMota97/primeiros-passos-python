# Contar a qtd de letras mais exibidas em uma frase
frase = "O rato roeu a roupa do rei de roma" \
"tres pratos de trigo para tres tigres tristes"
qtd_letra_maisvz = 0
letra_show_maisvz = ""
i = 0
while i < len(frase):
    letra_atual = frase[i]
    qtd_letra_show = frase.count(letra_atual)
    if letra_atual == " ":
        i+=1
        continue
    
    if qtd_letra_maisvz < qtd_letra_show:
        qtd_letra_maisvz = qtd_letra_show
        letra_show_maisvz = letra_atual
    i+=1
print(f"A letra que apareceu mais vezes foi {letra_show_maisvz} e foi exibida {qtd_letra_maisvz}x ")