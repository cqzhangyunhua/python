#coding=utf8
import csv
 
filename = './data/test.csv'
 
with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)

print(csvreader)