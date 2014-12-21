import csv
import re, sys
from collections import defaultdict
import threading, Queue
import time

'''reader = csv.reader(open("/home/zev/Desktop/testpractica/Maestra.csv" ,'rU'), delimiter=';')
for row in reader:
	print row.seek()'''


'''f = open("/home/zev/Desktop/testpractica/Maestra.csv", "rb")
f.seek(10, 1)
start = f.tell()
print start
s = f.readline() 
print s	'''

'''with open('/home/zev/Desktop/testpractica/Maestra.csv', 'rbU') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',')
     for row in spamreader:
         print row'''
'''g = open("/home/zev/Desktop/testpractica/Maestra.csv" ,'rbU') 
g.seek(800)




      
reader = csv.reader(g, delimiter=';')
for row in reader:
	print row[0]'''
	
	
	
	
FILE = "/home/zev/Desktop/testpractica/Maestra.csv"


def process(file, chunk):
	
    f = open(file, "rbU")
    f.seek(chunk[0])      
    reader = csv.reader(f, delimiter=';')
    for row in reader:
		##SQLLLLLLLLLL
    

    
    
def getchunks(file, size=1024*10):
    # yield sequence of (start, size) chunk descriptors
    f = open(file, "rbU")
    while 1:
        start = f.tell()
        f.seek(size, 1)
        s = f.readline() # skip forward to next line ending
        yield start, f.tell() - start
        if not s:
            break


class Worker(threading.Thread):
    def run(self):
        while 1:
            chunk = queue.get()
            if chunk is None:
                break    
            process(*chunk)
            queue.task_done()




	
	
queue = Queue.Queue()	
for i in range(4):
		w = Worker()
		w.setDaemon(1)
		w.start()
	
for chunk in getchunks(FILE):
		queue.put((FILE, chunk))

queue.join()
	

