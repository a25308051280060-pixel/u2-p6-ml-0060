import pandas as pd 
import numpy as np 
print("Ambar Fierro NC = 0060")
serie_amigos=["pedro", "morgan","farfan", "el adrian", "jesse", "eliseo", "mario"]
print("--- serie listado de amigos NC 0060---")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print("--- serie listado de billetes NC 0060---")
billetes=pd.Series(serie_billetes)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["veinte", "cincuenta","cien", "docientos", "quientos","mil" ]
print("--- serie listado nomre y valor de billetes NC 0060---")
tablabilletes=pd.Series(serie_bletras,serie_billetes)
print(tablabilletes)
# diccionario dataframe
# diccionario de valor de monedas y nombre
print(" datos de diccionario a datafren en pandas")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras": ["veinte", "cincuenta", "cien", "docinetos", "quinientos" , " mil"]
}

tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)

print("casa de cambio de Ambar Fierro NC = 0060")