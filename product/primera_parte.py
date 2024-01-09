# %%
import pandas as pd
import json
import os


#-----EXTRACCION-----#

#Lectura del archivo en formato JSON
directorio_actual= os.getcwd()
directorio_datos= os.path.join(directorio_actual,'data')
print(directorio_actual)
nombre_archivo_origen ='taylor_swift_spotify.json'

ruta_archivo_origen= os.path.join(directorio_datos,nombre_archivo_origen)

with open(ruta_archivo_origen, "r", encoding="utf8") as json_file:
    data = json.load(json_file)

#-----TRANSFORMACION-----#
#Creación del dataframe con la información contenida en el archivo .jason
df= pd.DataFrame(data)
#Extraccin y normalizacin de la columna 'albums' para la creación del dataframe con la informacion de los albumes
albums_df= pd.json_normalize(df.pop('albums'))

#Identificación de las columnas contenidas en el dataframe de los albumes
claves_albums_df = albums_df.keys()

#Creación de las columnas contenidas en el dataframe de albumes
df[claves_albums_df]=albums_df

#Extración de la información contenida en la columna tracks de dataframe principal
tracks_df= pd.json_normalize(df.iloc[0].pop('tracks'))
claves_df = df.iloc[0].keys()
tracks_df[claves_df]=df.iloc[0]


for i in range(1,len(df)):
    temp_tracks_df= pd.json_normalize(df.iloc[i].pop('tracks'))
    claves_df = df.iloc[i].keys()
    temp_tracks_df[claves_df]=df.iloc[i]
    tracks_df=pd.concat([tracks_df,temp_tracks_df],axis=0)

#Creación del dataframe final para la posterior exportación
dataset_df=tracks_df.drop('tracks',axis=1)
dataset_df.reset_index(inplace=True, drop=True)

#-----CARGA-----#

#Exportacion del dataframe final como archivo .csv

directorio_productos= os.path.join(directorio_actual,'product')
nombre_archivo_destino ='dataset.csv'

ruta_archivo_destino=os.path.join(directorio_productos,nombre_archivo_destino)
dataset_df.to_csv(ruta_archivo_destino,index=False)