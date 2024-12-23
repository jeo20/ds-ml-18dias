import findspark
findspark.init()

import random
from pyspark import SparkContext
sc = SparkContext(appName="CalcularValorPi")

def inside(p):
    x, y = random.random(), random.random()
    return x*x + y*y < 1
    
NUM_SAMPLES = 1000000
count = sc.parallelize(range(0, NUM_SAMPLES)).filter(inside).count()
print("El valor de Pi es: %f" % (4.0*count/NUM_SAMPLES))
sc.stop()

