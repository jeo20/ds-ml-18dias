class Book:
	def __init__(self, titulo, autor, anyo, descripcion):
		self.titulo = titulo
		self.autor = autor
		self.anyo = anyo
		self.descripcion = descripcion
		
	def toDBCollection (self):
		return {
			"titulo":self.titulo,
			"autor":self.autor,
			"anyo": self.anyo,
			"descripcion":self.descripcion
		}
		
	def __str__(self):
		return "Titulo: %s - Autor: %s - Anyo: %i - Descripcion: %s"%(self.titulo, self.autor, self.anyo, self.descripcion)

