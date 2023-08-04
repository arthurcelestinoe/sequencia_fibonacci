import sys
def while_fibo():
    control_exec = 1
    print("Olá seja bem-vindo ao Programa Gerador da sequência de Fibonacci!")
    while control_exec == 1:
        print("Para começarmos escolha uma das opções a seguir: \n[1] Quem foi Fibonacci? \n[2] O que é a sequência de Fibonacci e pra que ela serve? \n[3] Mostar sequencia de Fibonacci \n[4] Sair")
        opcao = int(input("Digite a opção desejada e tecle [enter]: "))

        if opcao == 1:
            print("\nLeonardo Fibonacci, também conhecido como Leonardo de Pisa, Leonardo Pisano ou ainda Leonardo Bigollo, (Pisa, c. 1170 — Pisa?, c. 1250) mais reconhecido como Fibonacci, foi um matemático italiano nomeado como o primeiro grande matemático europeu da Idade Média.\nÉ considerado por alguns como o mais talentoso matemático ocidental da Idade Média.\nFicou conhecido pela divulgação da sequência de Fibonacci e pela sua participação na introdução dos algarismos arábicos na Europa.")
            print("Para saber mais acesse: https://pt.wikipedia.org/wiki/Leonardo_Fibonacci\n")
        elif opcao == 2:
            print("\nNa matemática, a sucessão de Fibonacci (ou sequência de Fibonacci), é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual cada termo subsequente corresponde à soma dos dois anteriores.\nA sequência recebeu o nome do matemático italiano Leonardo de Pisa ou Leonardo Fibonacci, mais conhecido por apenas Fibonacci, que descreveu, no ano de 1202, o crescimento de uma população de coelhos, a partir desta.\nEsta sequência já era, no entanto, conhecida na antiguidade.")
            print("A sequência de Fibonacci tem aplicações na análise de mercados financeiros, na ciência da computação e na teoria dos jogos.\nTambém aparece em configurações biológicas, como, por exemplo, na disposição dos galhos das árvores ou das folhas em uma haste, no arranjo do cone da alcachofra, do abacaxi, ou no desenrolar da samambaia.\n")
            print("Para saber mais acesse: https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci\n")
        elif opcao == 3:
            print("Ok! Vamos calcular a sequêcia de Fibonacci")
            print("IMPORTANTE: Este programa gera a sequência de Fibonacci de seu principio até a posição especificada por você.\nNão é possivel utiliza-lo para exibir um único elemento da sequência.\n \n")
            print("Digite a posição final pretendida da sequência de Fibonacci")
            posicao_final = int(input("Digite o número correspondente aqui e pressione [enter]: "))
            internal_control = 1
            f1, f2 = 1, 1
            num_sequencia = 1
            while internal_control <= posicao_final:
                print(f"{internal_control}º posição= {num_sequencia}")
                num_sequencia = f1 + f2
                f2 = f1
                f1 = num_sequencia
                internal_control += 1
        elif opcao == 4:
            sys.exit("Obigado por usar o Gerador da Sequência de Fibonacci!\nAté mais!")
        else:
            print("Opção inválida! Tente novamente!\n \n")
        
        text = str(input("Deseja continuar? [S ou s para continuar ou qualquer outra tecla para encerrar]: "))
        if text == "S" or text == "s":
            print("Ok!")
        else:
            print("Obigado por usar o Gerador da Sequência de Fibonacci!\nAté mais!")
            control_exec = 0
while_fibo()
