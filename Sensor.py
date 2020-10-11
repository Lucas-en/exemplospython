
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db =client['bancofabrica']
sensores = db.sensores

# Importando Threading
import threading
# Importando time para controlar tempo da thread
import time
# Importando random para gerar números aleatóreos
import random


# Função que simula valores para cada Thread
def simulaTemp(nome, numero, intervalo,):
    while True:
        valor = random.randint(30, 40)
        print(nome, numero, ':', valor)
        time.sleep(intervalo)
        result = sensores.update_one(
             {'nome': 'Temperatura ' + str(numero)},
             {'$set': {'valor': valor}}
        )
        if valor > 38:
            resultt = sensores.update_one(
                {'nome': 'Temperatura ' + str(numero)},
                {'$set': {'tevealarme': True}}
            )
        else:
            resultt = sensores.update_one(
                {'nome': 'Temperatura ' + str(numero)},
                {'$set': {'tevealarme': False}}
            )
        if result.acknowledged:
            print('Valor de', nome, numero, 'atualziado no banco!')
        if valor > 38 and result.acknowledged:
            print('True')


# Abrindo a 1ª Thread
x = threading.Thread(target=simulaTemp, args=('Temperatura', 1, 2))
x.start()

# Abrindo a 2ª Thread
y = threading.Thread(target=simulaTemp, args=('Temperatura', 2, 3))
y.start()

# Abrindo a 3ª Thread
a = threading.Thread(target=simulaTemp, args=('Temperatura', 3, 4))
a.start()

# Abrindo a 4ª Thread
b = threading.Thread(target=simulaTemp, args=('Temperatura', 4, 5))
b.start()

