import pandas as pd
import numpy as np

import findspark
findspark.init()

import pyspark
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

import databricks.koalas as ks

ks_df = ks.read_csv("movies.csv", sep=',')
print(ks_df.shape)
print(ks_df.dtypes)
print(ks_df.columns)
print(ks_df.head())
