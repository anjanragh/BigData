import sys
from pyspark import SparkContext
from csv import reader

sc = SparkContext()
lines = sc.textFile(sys.argv[1], 1)
lines = lines.mapPartitions(lambda x: reader(x))
lines = lines.map(lambda x: (x[2],1)).reduceByKey(lambda x,y:x+y)
lines = lines.map(lambda x: (str(x[0])+"\t"+str(x[1])))
lines.saveAsTextFile("task2.out")
