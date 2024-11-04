import random
inicio = input("Queres jogar este jogo?: ")
inicio = inicio.lower ()
if inicio == "sim":
  nome = input ("Entao digite o seu nome: ")
  print  (f"\nNum dia chuvoso de noite, {nome}, voltava para casa com 3 amigos no seu carro, Victor, Hugo e o Vitinha. Até que a estrada a esquerda que era o caminho para casa estava cortada por um carro da polícia por causa da queda de uma arvore!")
  escolha1 = input(f"\n{nome}, queres continuar para a esquerda e desobedecer a Polícia ou seguir pelo caminho da direita?: ")
  escolha1 = escolha1.lower ()
  if escolha1 == "esquerda":
    print(f"\n{nome} desobedece a policia atropela 2 policias e espeta-se contra a arvore! Fica gravemente ferido e com uma sentença a prisão perpétua!!!" "\n\nFIM!")
  elif escolha1 == "direita":
    print(f"\n{nome} segue pelo caminho da direita que leva a uma estrada com uma floresta muito densa, e muito escura.")
    print (f"\n{nome} vai conduzindo com muito cuidado e lentamente por uma rua de terra batida, ao começo {nome} e os seus amigos estavam com medo mas conforme vao avançando, encontram um vilarejo muito pequeno com um café mas com um aspeto duvidoso então Vitinha pede a {nome} para parar porque precisa de ir a casa de banho.")
    escolha2 = input("Quer parar o carro para deixar Vitinha fazer as suas necessidades basicas?: ")
    escolha2 = escolha2.lower ()
    if escolha2 == "sim":
        print(f"\n{nome} para o carro porque Vitimha precisa de ir a casa de banho da loja com um aspeto meio duvidoso, entao Vitinha entre na loja e nota algo diferente no atendente, parecia meio morto muito frio, mas como ele estava com vontade continua e vai na mesma. Mas {nome}, Victor e Hugo não o deixam ir sozinho então vão atras de Vitinha, ao entrarem na loja ocorre um apagão. A loja fica toda escura e ouve-se uma porta a abrir e a fechar rapidamente, então que a loja começa a pegar fogo e {nome} e os seus amigos começam a queimar e acabam por bater as botas!!!" "\n\nFIM!")
    elif escolha2 == "não":
        print(f"{nome} ignora vitinha e segue o seu caminho.")
        print(f"\n{nome} ao continuar o caminho para casa, o carro fica sem gasoleo e Victor então da ideia de irem a pé já que afinal faltavam mais ou menos uns 500m para chegar a casa. Então acabam por deixar o carro e irem." "\nSo que no meio dessa curta caminhada eles ouvem uma voz feminina no meio da floresta a gritar por ajuda.")
        escolha3 = input(f"{nome} queres ajudar a senhora ou continuar a ir para casa?")
        escolha3 = escolha3.lower ()
        if escolha3 == "não":
            print("Continua o caminho para casa e chega seguro a casa!!!" "\n\nConseguiu acabar o jogo 100%" "\n Parabéns!" "\nFIM!")
        elif escolha3 == "sim":
            print(f"\n{nome} decide ir ajudar a rapariga, os seus amigos um bocado receosos não queriam ir, mas acabaram por acompanhar {nome}.")
            print(f"\n {nome} ao chegar perto do local de onde se ouvia os gritos! Até que se repararam com um caminho de velas pelo meio da floresta, no meio das arvores." f"\n{nome} ao ver o caminho eles ficam curiosos.")
            escolha4 = input("Quer continuar e seguir o caminho de velas para ajudar a rapariga ou arrepende-se e quer voltar para tras?(ir/voltar):")
            escolha4 = escolha4.lower
            if escolha4 == "voltar":
                print (f"{nome} volta para tras mas acidentalmente, derruba uma vela e com efeito domino as velas vão caindo em efeito domino e acaba por incendiar a floresta inteira." f"\n {nome} acaba por morrer quiemado!!" "\n\nFIM!!")
            elif escolha5 == "ir":
                print (f"{nome} curioso avança para ajudar a rapariga!")
                print (f"Ao chegar perto da rapariga, reparam que ela ja estava morta, e então decidem voltar mas ao voltar encontram o assasino da rapariga, que no fim acaba por os matar!" "\n\nFIM!" "\nPERDESTE!")
                
        
           
           
           
           
           
else: 
  print ("FIM!")



