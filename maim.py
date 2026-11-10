import random
print("Bem vindo ao jogo da imaginação")
print("1 - Um carro que anda sobre a água", "2 - Uma escola dentro de uma nave espacial","3 - Um relógio que volta 10 segundos no tempo")
while True:
  escolha_socre = int(input("Digite sua imaginação em numero Ex: 1,2 ou 3:"))
  if escolha_socre == 1:
    print("Voce escolheu o 1 - Um carro que anda sobre a água" )
    break
  elif escolha_socre == 2:
    print("Voce escolheu o 2 - Uma escola dentro de uma nave espacial ")
    break
  elif escolha_socre == 3:
    print("Voce escolheu o  3 - Um relógio que volta 10 segundos no tempo")
    break
      

print (" 1- Um robô que organiza a geladeira sozinho"," 2- Uma ilha que só aparece à meia-noite"," 3- Um espelho que mostra seu eu do futuro")
imagina = random.randint(1 , 3)
if escolha_socre == imagina:
      print("acertou Parabens")

