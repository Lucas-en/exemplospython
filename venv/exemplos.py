
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db =client['bancofabrica']
sensores =db.sensores

#criando documento novo
sensor ={
    'nome':'Temperatura 1',
    'valor':39,
    'unidade': 'ºC'
    'teve alarme': 'false',
}

#Inserindo documento no MongodB
result = sensores.insert_one(sensor)
# verificando se deu certo o programa
if result.acknowledged:
    print('Sensor adicionado  Sensor Id',
            result.inserted_id)
else:
    print ('Deu errado')
