#Calculadora de plantões
def calculadora_plantao():
    select_meses = input("Selecione o mês desejado............................................: ")
    meses_do_ano = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

    mes = select_meses.upper()

    if select_meses in meses_do_ano:
        print(f'Você selecionou o mês de {mes}. ')

        select_plantao = int(input("Selecione o plantão desejado........................................: "))
        plantao = [12, 24]

        if select_plantao in plantao:
            print(f'Plantão {select_plantao}h selecionado. ')

            if select_plantao == 12:
                select_valor_12 = float(input("Informe o valor do plantão 12h......................................: "))
                select_valor_12_format = "{:.2f}".format(select_valor_12)
                print(f'O valor do plantão informado é de R$ {select_valor_12_format}. ')

                dias_trabalhados_12 = int(input(f"Informe a quantidade de dias trabalhados no mês selecionado.........: "))
                plantao_12 = dias_trabalhados_12 * select_valor_12
                plantao_12_format = "{:.2f}".format(plantao_12)
                print(f"{dias_trabalhados_12} plantões de 12h realizados no mês de {mes} correspondem a R$ {plantao_12_format}. ")

            elif select_plantao == 24:
                select_valor_24 = float(input("Informe o valor do plantão 24h......................................: "))
                select_valor_24_format = "{:.2f}".format(select_valor_24)
                print(f'O valor do plantão informado é de R$ {select_valor_24_format}. ')

                dias_trabalhados_24 = int(input(f"Informe a quantidade de dias trabalhados no mês selecionado.........: "))
                plantao_24 = dias_trabalhados_24 * select_valor_24
                plantao_24_format = "{:.2f}".format(plantao_24)
                print(f"{dias_trabalhados_24} plantões de 12h realizados no mês de {mes} correspondem a R$ {plantao_24_format}. ")

            else:
                print("Informe um valor correto! ")

        else:
            print("Informe uma opção correta! ")
    else:
        print("Informe uma opção correta!")

while True:    
    calculadora_plantao()

