def metrage_limpeza():
    print("-" * 15 + "Menu 1 de 3 - Metragem da limpeza" + "-" * 15)
    while True:
        try:
            metragem = int(input("Digite a metragem desejada da limpeza:"))

            if (metragem >= 30) and (metragem < 300):
                print("É necessário contratar 1 pessoa")                          #Coloquei os if verificando segundo a tabela e a mensagem de contratar 1 ou 2 pessoas num while
                return 60 + metragem * 0.3

            elif (metragem >= 300) and (metragem < 700):
                print("É necessario contratar 2 pessoas")
                return 120 + metragem * 0.5
            else:
                print("Nossa empresa nao aceita mais que 30m² ou mais que 700 m².")
                continue
        except ValueError:
            print('Digite os m² apenas com números inteiros!')

def tipo_limpeza():
    print("-" * 15 + "Menu 2 de 3 - Tipo da limpeza" + "-" * 15)
    while True:
        print("B - Básica Indicada para sujeiras semanais \nC - Completa Indicada para sujeiras antigas")
        tipo = input("Entre com o tipo de limpeza:")
        if tipo == 'B':
            print("Você selecionou a limpeza Básica!")              #Nessa função verifiquei novamente com if qual tipo de limpeza
            return 1.0
        elif tipo == 'C':
            return 1.3
        else:
            print("Digite apenas a letra B ou C!")
            continue

def adicional_limpeza():
    print("-" * 15 + "Menu 3 de 3 - Adicionais da limpeza" + "-" * 15)
    total_adicionais = 0
    while True:
        print("0 - Não desejo mais nada obrigado (encerrar)\n1 - Passar 10 peças de roupa - R$10,00\n2 - Limpeza de um Forno/Micro-ondas - R$12,00\n3 - Limpeza de uma Geladeira/Freezer - R$20,00")
        adicional = input("Deseja mais algum adicional?")

        if adicional == '0':
            return total_adicionais
        elif adicional == '1':
            total_adicionais += 10
        elif adicional == '2':                         #Nessa função criei um "acumulador" que retorna o total para o usuario o final após digitar '0'
            total_adicionais += 12
        elif adicional == '3':
            total_adicionais += 20
        else:
            print("Digite apenas os números 0 (Encerrar) 1, 2 e 3 para adicionais.")

print("Bem vindo ao Programa de Serviços de Limpeza do Rubens Junior")
metragem_final = metrage_limpeza()
tipo_final = tipo_limpeza()                                            # E por último coloquei nome da função de cada um e apresentei em um ultimo print o total.
adicionais_final = adicional_limpeza()
total_final = (metragem_final * tipo_final + adicionais_final)
print("Total do serviço: R$:{:.2f} (Metragem :{} * tipo:{} + adicional:{})".format(total_final,metragem_final,tipo_final,adicionais_final))





