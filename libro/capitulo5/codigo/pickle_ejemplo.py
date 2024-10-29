import pickle

datos = {
    'lenguajes': ['Python', 'Java','JavaScript'],
    'booleanos': {None, True, False}
}

with open('datos.pickle', 'wb') as fichero:
    pickle.dump(datos, fichero)
    
   
with open('datos.pickle', 'rb') as fichero:
	datos = pickle.load(fichero)
	print(datos)


