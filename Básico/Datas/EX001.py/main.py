#Carregue a data atual do computador e apresente somente a data
import datetime 
data_atual = datetime.datetime.now()
print(data_atual.strftime("%x"))
#Carregue a data atual do computador e, com base na data atual, apresente a data de dois dias no futuro
data_2_dias = datetime.timedelta(days=2) 
data_futura = data_atual + data_2_dias 
print(data_futura.strftime("%x"))