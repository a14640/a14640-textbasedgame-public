import random
inicio = input("Voce quer jogar este jogo?: ")
inicio = inicio.lower ()
if inicio == "sim":
  nome = input ("Entao digite o seu nome: ")
  print  (f"\nNum dia chuvoso de noite, {nome}, voltava para casa com 3 amigos no seu carro, Victor, Hugo e o Biru. Até que a estrada a esquerda que era o caminho para casa estava cortada pela polícia por causa da queda de uma arvore!")
  escolha1 = input(f"\n{nome}, queres continuar para a esquerda e desobedecer a Polícia ou seguir pelo caminho da direita?: ")
  if escolha1 == "Esquerda":
    print(f"\n{nome} desobedece a policia atropela 2 policias e espeta-se contra a arvore! Não morre, mas fica sentenciado a prisão perpétua!!!")
    
else: 
  print ("FIM!")

