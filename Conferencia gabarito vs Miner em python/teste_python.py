#importa pacote para requisições JSON
import json, requests
#importar biblioteca para gravar arquivo de saída
from baseTesteBOs import BaseTesteBOsDAO
from minerAPI import MinerAPI
from csvUtils import CsvUtils
from latLong import LatLong

def main():
#Descobrir quais as facets da collection
    collection = 'col_68976'
#classes externas    
    miner = MinerAPI()
    baseSql = BaseTesteBOsDAO()
    texto = CsvUtils()
    latlongitude = LatLong()

#buscar facets   
    stringfacets = miner.collectionFacets(collection) 
#buscar BOs na base SQLite
    retornoSqlTodos = baseSql.baseBOs()

#    lista = []
    listaExtensa1 = []

    for retornoSql in retornoSqlTodos:
#validar no miner
        lista1=[]
        listaExtensa = []
        retornoSql1 = []
        facetsDict = miner.busca_facet(retornoSql[0],retornoSql[1],retornoSql[2],stringfacets,collection)
#monta os dados para consulta        
        lista1.append(retornoSql[0])
        lista1.append(retornoSql[1])
        lista1.append(retornoSql[2])

        if facetsDict != '':
    # SE ENCONTRAR DADOS NO MINER
#buscar dados de latitude + longitude + autoria
            camposDeIndice = miner.camposDeIndice(retornoSql[0],retornoSql[1],retornoSql[2],stringfacets,collection)
            latilong_calc = latlongitude.latLong(camposDeIndice)
            numSimilar = miner.capturaSimilares(collection, latilong_calc, camposDeIndice['autoria_bo'], facetsDict['facetsString'], facetsDict['string_similar'])
            del facetsDict['string_similar']
            del facetsDict['facetsString']
            for key,value in facetsDict.items():
                lista1.append(value)
    #montar lista de listas com os dados para gravação
            retornoSql1.append(retornoSql[3])
            retornoSql1.append(retornoSql[4])
            retornoSql1.append(retornoSql[5])
            retornoSql1.append(retornoSql[6])
            retornoSql1.append(retornoSql[7])
            retornoSql1.append(retornoSql[8])
            retornoSql1.append(retornoSql[9])
            retornoSql1.append(retornoSql[10])
            retornoSql1.append(retornoSql[11])

            lista2 = lista1[3:]
    #adiciono porque quero começar da quarta coluna para frente
            for i in range(len(lista2)):
                if lista2[i] == 1 and retornoSql1[i] == 1:
                    listaExtensa.append('OK')
                elif lista2[i] == 0 and retornoSql1[i] == 0:
                    listaExtensa.append('NP')
                else:
                    listaExtensa.append("NOK")
            
            a = (lista1[:3]+listaExtensa)
            a.append(numSimilar)
            listaExtensa1.append(a)
        else:
            pass


#        listaExtensa1.append(listaExtensa)
#        lista.append (lista1)
    
#gravar cvs com o resultado  
    texto.montarCsv(listaExtensa1)

#gravar resultado no banco
    baseSql.gravaBOs(listaExtensa1)


if __name__ == "__main__":
    main()