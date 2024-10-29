from pymongo import MongoClient
from Book import Book

# Creo una lista de objetos a insertar en la BD
books = [
    Book('MongoDB','author',2019,'MongoDB'),
    Book('Cassandra','author',2020,'Cassandra'),
    Book('Neo4j','author',2021,'Neo4j'),
    Book('ElasticSearch','author',2022,'Elastic')
]

# PASO 1: Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)
print(mongoClient)
# PASO 2: Conexión a la base de datos
db = mongoClient.Book
print(db)
# PASO 3: Obtenemos una colección para trabajar con ella
collection = db.Books
print(collection)

# PASO 4: "CREATE”
for book in books:
	print(book.toDBCollection())
	collection.insert_one(book.toDBCollection())

# PASO 5:Obtener el número documentos
print(collection.count_documents({}))

# PASO 6: "READ" -> Leemos todos los documentos de la base de datos
cursor = collection.find()
for book in cursor:
    print(book['titulo'], book['autor'], book['anyo'], book['descripcion'])

# PASO 7: "UPDATE" -> Actualizamos la descripción de los libros.
collection.update_many({"anyo":{"$gt":2020}},{"$set":{"descripcion":"nueva descripcion"}}, upsert = False)

# PASO 8: "DELETE" -> Borramos todos los libros donde  anyo=2019
collection.delete_one({"anyo":2019})

