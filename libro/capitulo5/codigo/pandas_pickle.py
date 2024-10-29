import pandas as pd

datos = {
    'lenguajes': ['Python', 'Java','JavaScript'],
    'booleanos':[None, True, False]
}

df = pd.DataFrame(datos)

# guardar un dataframe de pandas como objeto pickle en un fichero
df.to_pickle('fichero_pickle.pickle') 

# recuperar el dataframe a partir del fichero
df= pd.read_pickle('fichero_pickle.pickle')

print(df)

