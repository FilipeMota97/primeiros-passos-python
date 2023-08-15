velocidade = 100
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if local_carro >= (LOCAL_1 - RADAR_RANGE) and (LOCAL_1 + RADAR_RANGE):
    if velocidade > RADAR_1:
        print(f"Seu carro passou pelo Radar 1 com a velocidade de {velocidade} e foi multado pois o limite de velocidade é de {RADAR_1} ")
    else:
        print("Seu carro passou pelo Radar 1 e não foi multado")