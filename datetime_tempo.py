from datetime import datetime

'''print(datetime.now())
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

#criar uma data
lancamento_app = datetime(2021, 5, 28)
print(lancamento_app)
#quero receber a data lançamento do meu aplicativo
#25/08/2020
data_de_lançamento = datetime.strptime(input('Quando devemos lançar o aplicativo?'),'%d/%m/%Y')
print(type(data_de_lançamento))

#quanto tempo você possui até a data de lançamento
#assim você pode calcular o intervalo entre datas
data_atual = datetime.now()
prazo = data_de_lançamento - data_atual
print(prazo.days, 'dias')
'''



#Desafio
data_aniversario = datetime(2023, 2, 18)
data_atual = datetime.now()
prazo = data_atual - data_aniversario
print(f"faltam {prazo.days}, dias para meu aniversário")


aniversario = datetime(2023, 2, 18)
dias_para_aniversario = aniversario - datetime.now()
print(dias_para_aniversario)