from datetime import date, datetime

# data = date(2024, 6, 6)
# print(data)
# print(date.today())

# data_hora = datetime(2024, 6, 6, 23, 59, 59)
# print(data_hora)

data_hora = datetime.today()
hora = data_hora.time()
print(hora)
