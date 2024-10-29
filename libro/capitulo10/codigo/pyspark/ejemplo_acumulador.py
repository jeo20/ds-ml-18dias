from pyspark import SparkContext
sc = SparkContext("local[*]","My app")

file_rdd = sc.textFile("test.log")

lineasBlanco = sc.accumulator(0)

def extraerLineasBlanco(line):
	global lineasBlanco
	if(line==''):
		lineasBlanco+=1
	return line

resultado = file_rdd.map(extraerLineasBlanco)

print("Total de lineas/Lineas en Blanco fichero test.log:",resultado.count(),"/",lineasBlanco.value)

