#Pegar hora atual 
import datetime 
data_atual = datetime.datetime.now()
print(data_atual.strftime("%x"))
#Com a data apresentar a data que será daqui a 2 dias 
data_2_dias = datetime.timedelta(days=2) 
data_futura = data_atual + data_2_dias 
print(data_futura.strftime("%x"))