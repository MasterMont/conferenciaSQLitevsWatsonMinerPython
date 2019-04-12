import math
from datetime import date
'''
#class LatLong:

#def latLong(self,dicio_latlong):
lati = dicio_latlong['latitude']
longi = dicio_latlong['longitude']
raio = 6371 '''
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
#distancia = 15/raio
'''
angulo = [90,-90]

for i in angulo:
    latitudeDestino  = math.asin(math.sin(lati)*math.cos(distancia) + math.cos(lati)*math.sin(distancia) * math.cos(i))
    print('Latitude final %s' % (lati + latitudeDestino))

   ''' '''
    Then calculate the new longitude, using your result for lat2:

    var λ2 = λ1 + Math.atan2(Math.sin(brng)*Math.sin(d/R)*Math.cos(φ1) , Math.cos(d/R)-Math.sin(φ1)*Math.sin(φ2));
    ''''''
    xd = math.atan2(math.sin(i) * math.sin(distancia)*math.cos(lati) , math.cos(distancia) - math.sin(lati) *math.sin(latitudeDestino))
    longitudeDestino = longi + xd #math.atan2(math.sin(i) * math.sin(distancia)*math.cos(fuk) , math.cos(distancia) - math.sin(fuk1) *math.sin(latitudeDestino))
    print('Longitude final %s' % longitudeDestino)
    retorno = {(lati + latitudeDestino): longitudeDestino}

return retorno
'''
GAP_LAT = 0.00089933
GAP_LNG = 0.00098033

lat1 = 23.5121185703387 - (GAP_LAT * 15) #// LAT_SUP
lat2 = 23.5121185703387 + (GAP_LAT * 15) #// LAT_INF
lng1 = 46.6667005134495 - (GAP_LNG * 15) #// LNG_SUP
lng2 = 46.6667005134495 + (GAP_LNG * 15) #// LNG_INF
print(lat1,lat2,lng1,lng2)
#LatLng point1 = new LatLng(lat1, lng1)
#LatLng point2 = new LatLng(lat2, lng2)

data = date.today()
novaData = data.strftime('%d/%m/%Y')
print(novaData)