import json,requests

class MinerAPI:
    #chamada para verificar quais as facets da collection
    def collectionFacets(self,collection):
        response = requests.get ('http://10.75.200.221:8393/api/v10/facets?collection='+collection+'&output=application/json&namespace=subfacet')
    #monta string com as facets para consulta
        resultadoString = ''
        resposta = json.loads(response.content)
        data_dict = resposta["ibmbf_facets"]
        data_lista = data_dict["ibmbf_facet"]
        resposta_dict = data_lista[3]
        resposta_final = resposta_dict["ibmbf_facet"]
        for i in range(len(resposta_final)):
            xy = resposta_final[i]
            resultadoString+=(xy["id"]+'|')
        return resultadoString[:-1]

 #buscar o dado no Miner
    def busca_facet(self,delegacia,ano,numero_bo,stringfacets,collection):
        facetsString = []
        delegacia_string=str(delegacia)
        ano_string=str(ano)
        bo_string=str(numero_bo)
        query_monta = "&query=id_delegacia: "+delegacia_string+" AND ano_bo: "+ano_string+" AND num_bo: "+bo_string
        
# monta lista de string para chamado dos similares        
        string_para_similares = []
        string_para_similares.append(delegacia_string)
        string_para_similares.append(ano_string)
        string_para_similares.append(bo_string)
        chamada = 'http://10.75.200.221:8393/api/v10/search/facet?output=application/json&collection='+collection+'&facet={"namespace":"keyword","id":"'+stringfacets+'"}'+query_monta
 #chamado para o miner com dados
        resposta_miner = requests.get(chamada)

 #tratamento de erro necessário
        if(resposta_miner.status_code != 200):
            print(resposta_miner.content)
        else:
            data_miner = json.loads(resposta_miner.content)
            limpa_data_miner = data_miner["es_apiResponse"]
            if limpa_data_miner == None:
                print("dados não encontrados no miner para %s" %query_monta)
                return ''

#Montar uma string com as facets para futura consulta dos Similares                
            for i in limpa_data_miner['ibmsc_facet']:
                string_para_similares.append(i["label"])
            
            facetsString.append(string_para_similares)
########
######## Transformar o resposta em 0 e 1 para comparação
            retorno = {
                'nAutor': 0,
                'nAutorAcaoFugir': 0,
                'nAutorAcaoAbordagem': 0,
                'nQtdAutor': 0,
                'nArmaFogo': 0,
                'nAutorAcaoCoacao': 0,
                'nAutorAcaoSubtrair': 0,
                'nAutorAcaoAgressao': 0,
                'nArmaBranca' : 0
            }
            #
            autorLabel = []
            #
            for row in limpa_data_miner['ibmsc_facet']:
                retorno[row['label']] = retorno[row['label']] + 1

                if row['label'] == 'nAutor':
                    x = row['ibmsc_facetValue']
                
                    if type(x) != dict:

                        for i in x:
                            autorLabel.append(i['label'])

                    else:
                        autorLabel.append(x['label'])

            retorno.update({'facetsString' : string_para_similares})
            retorno.update({'string_similar' : autorLabel})
            return retorno

#Campos de indice para cada BO
    def camposDeIndice(self,delegacia,ano,numero_bo,stringfacets,collection):
        delegacia_string=str(delegacia)
        ano_string=str(ano)
        bo_string=str(numero_bo)
        query_monta = "&query=id_delegacia: "+delegacia_string+" AND ano_bo: "+ano_string+" AND num_bo: "+bo_string
        resposta_miner = requests.get('http://10.75.200.221:8393/api/v10/search/feed/entry?output=application/json&collection='+collection+'&returnedField={"|autoria_bo|latitude|longitude|"}'+query_monta)

# TRATAMENTO DE ERRO
        if(resposta_miner.status_code != 200):
            print(resposta_miner.content)
#
        else:
            data_miner = json.loads(resposta_miner.content)
            limpa_data_miner = data_miner["es_apiResponse"]
            dados_limpos = limpa_data_miner["es_result"]
            dados_limpos_final = dados_limpos['ibmsc_field']

        retorno = {}

        for key in dados_limpos_final:
            retorno.update({(key['id']):(key['#text'])})
            
                
        return retorno
# pegar o numero de registros similares no Miner
    def capturaSimilares( self, collection, dicio_similar, autoria, facetsString, stringAutor):
        latitudeMenor = str(dicio_similar[0])
        latitudeMaior = str(dicio_similar[1])
        longitudeMenor= str(dicio_similar[2])
        longitudeMaior= str(dicio_similar[3])
        facetsSimilares = ''
        facetsIterar = facetsString[3:]
        a = 0
        for i in facetsIterar:
            if i == 'nAutor':
                pass
            else:
                facetsSimilares += ('(subfacet::/"parsing_rules"/"'+i+'") AND ')

        if 'nAutor' in facetsIterar:
            facetsSimilares += ('(')
            for y in stringAutor:
                a += 1
                facetsSimilares += ('/"keyword$.parsing_rules.nAutor"/"'+y+'"')
                if a != len(stringAutor):
                    facetsSimilares += ' OR '
                else:
                    facetsSimilares += ')'



        chamada = "http://10.75.200.221:8393/api/v10/search?output=application/json&collection="+collection+"&pageSize=30&page=1\
&summaryLengthRatio=500&returnedField='nome_delegacia|id_delegacia|ano_bo|num_bo|latitude|longitude|autoria_bo&query=(latitude > "+latitudeMenor+"\
 AND latitude < "+latitudeMaior+" AND longitude > "+longitudeMenor+" AND longitude < "+longitudeMaior+") AND (autoria_bo: "+autoria+") AND "+facetsSimilares
        
        resposta_miner = requests.get(chamada)
        if(resposta_miner.status_code != 200):
            print(resposta_miner.content)
            print(resposta_miner.status_code)
        else:
            data_miner = json.loads(resposta_miner.content)
            limpa_data_miner = data_miner["es_apiResponse"]
            if limpa_data_miner == None:
                print("dados não encontrados no miner")
                return ''
            else:
                return limpa_data_miner["es_totalResults"]