from pyspark import SparkContext
sc = SparkContext("local[*]","My app")

file_rdd = sc.textFile("test.log")

my_broadcast_variable = sc.broadcast({200:'OK',401:'Bad Request',404:'Not Found',505:'Server error'})

def extraerCodigoEstado(line):
	tokens = line.split(" ")
	if len(tokens)>7:
		return (my_broadcast_variable.value[int(tokens[8])],1)
	else:
		return("",1)
        
codigosEstado = file_rdd.map(extraerCodigoEstado).groupByKey()

for line in codigosEstado.collect():
	print("Código estado:",line[0],"-->",sum(line[1]))

