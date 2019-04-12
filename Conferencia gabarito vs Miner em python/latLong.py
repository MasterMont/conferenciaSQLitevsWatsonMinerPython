import math

class LatLong:

    def latLong(self,dicio_latlong):
        lati = float(dicio_latlong['latitude'])
        longi = float(dicio_latlong['longitude'])
        #raio = 6371 
        retorno = set()
        distancia = 15 #deverá ser em hectômetros(hm), ou seja 5.0 corresponde 500 metros
        GAP_LAT = 0.00089933
        GAP_LNG = 0.00098033

        lat1 = lati - (GAP_LAT * distancia) #// LAT_SUP
        lat2 = lati + (GAP_LAT * distancia) #// LAT_INF
        lng1 = longi - (GAP_LNG * distancia) #// LNG_SUP
        lng2 = longi + (GAP_LNG * distancia) #// LNG_INF

        retorno.add(lat1)
        retorno.add(lat2)
        retorno.add(lng1)
        retorno.add(lng2)
        
        return sorted(retorno)
    #raio da terra
    # Você tem graus decimais (-73.9874°), em vez de graus, minutos e segundos (-73° 59’ 14.64 ") 
    # As unidades inteiras de graus permanecerá o mesmo 
    #(-73.9874° de longitude, comece com 73°) # Multiplique o decimal por 60 (0.9874 * 60 = 59.244) 
    # O número total torna-se o minuto (59’) 
    # Leve o restante decimal e multiplicar por 60. (0.244 * 60 = 14.64) # O número resultante torna-se o segundo (14.64). 
    #Seconds pode permanecer como um decimal. 
    # Tome seus três conjuntos de números e colocá-los em conjunto, utilizando os símbolos para graus (º), minutos (’) e segundos (") (-73° 59’ 14,64" de longitude) 
    #'''
    #var φ2 = Math.asin( Math.sin(φ1)*Math.cos(d/R) + Math.cos(φ1)*Math.sin(d/R)*Math.cos(brng) );
    #
    #var λ2 = λ1 + Math.atan2(Math.sin(brng)*Math.sin(d/R)*Math.cos(φ1) , Math.cos(d/R)-Math.sin(φ1)*Math.sin(φ2));
    #'''

#Define alpha = dist/[earth radius] to be the angular distance covered on the earth's surface.
"""     distancia = 15/raio

        angulo = [0,90,180,-180]
        retorno = set()
        retornoLat = set()
        retornoLong = set()
        for i in angulo:
            latitudeDestino  = math.asin(math.sin(lati)*math.cos(distancia) + math.cos(lati)*math.sin(distancia) * math.cos(i))
            
            retornoLat.add(lati + latitudeDestino)
            '''
            Then calculate the new longitude, using your result for lat2:

            var λ2 = λ1 + Math.atan2(Math.sin(brng)*Math.sin(d/R)*Math.cos(φ1) , Math.cos(d/R)-Math.sin(φ1)*Math.sin(φ2));
            '''
            xd = math.atan2(math.sin(i) * math.sin(distancia)*math.cos(lati) , math.cos(distancia) - math.sin(lati) *math.sin(latitudeDestino))
            longitudeDestino = longi + xd #math.atan2(math.sin(i) * math.sin(distancia)*math.cos(fuk) , math.cos(distancia) - math.sin(fuk1) *math.sin(latitudeDestino))

            retornoLong.add(longitudeDestino)
"""
