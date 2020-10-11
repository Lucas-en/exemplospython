

#importando o pymongo
from pymongo import MongoClient
import pprint
#criando/acessando uma conexão
client = MongoClient('mongodb://localhost:27017')
#criando/acessando um database
db =client['bancofabrica']
#criando/acessando uma coleçao
sensores =db.sensores
# Buscando documentos
results = sensores.find()
#Varrendo os documentos
for aux in results:
    pprint.pprint(aux)
