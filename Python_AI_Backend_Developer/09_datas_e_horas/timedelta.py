from datetime import datetime, timedelta


data_atual = datetime.utcnow()
data_atual += timedelta(minutes=10)
print(data_atual.time())
