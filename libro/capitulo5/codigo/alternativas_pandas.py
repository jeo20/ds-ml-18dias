#pip install datatable
import datatable
 
#leer csv
data_frame = datatable.fread("airports.csv", header = None)
print(data_frame.head())

#seleccion de columnas
data_frame2 = data_frame[:,['name','abbrev']]
print(data_frame2.head(5))

#ordenar datos por una columna
ordenar = data_frame.sort('name')
print(ordenar.head(5))

#pip install modin
import modin.pandas as pd

#leer csv
data_frame = pd.read_csv("airports.csv")
print(data_frame.head())

#pip install pyarrow
from pyarrow import csv

data_frame = csv.read_csv("airports.csv")
print(data_frame)
print(data_frame.schema)
print(data_frame['name'])

#seleccion de columnas
print(data_frame.select(["name", "abbrev"]))
print(data_frame.slice(0,10).to_pandas())

#pip install vaex
import vaex
data_frame = vaex.example()
print(data_frame.describe())

#pip install polars
import polars as pl

data_frame = pl.read_csv("airports.csv")
print(data_frame.head(5))
print(data_frame.describe())
