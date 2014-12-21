# chunked access from multiple processes.  the chunking and parallelization
# stuff can be used for any similar problem (and should probably be moved to
# a support library)

import re, sys
from collections import defaultdict

import threading, Queue, subprocess
import marshal, struct

# configuration

try:
    CPUS = int(sys.argv[1])
except:
    CPUS = 2

executable = [sys.executable]
if sys.platform == "win32":
    executable.append("-u") # use raw mode on windows

def process(file, chunk):
    f = open(file, "rb")
    f.seek(chunk[0])
    print "hola"

def getchunks(file, size=1024*10):
    # yield sequence of (start, size) chunk descriptors
    f = open(file, "rb")
    while 1:
        start = f.tell()
        f.seek(size, 1)
        s = f.readline() # skip forward to next line ending
        yield start, f.tell() - start
        if not s:
            break

def putobject(file, object):
    data = marshal.dumps(object)
    file.write(struct.pack("I", len(data)))
    file.write(data)
    file.flush()

def getobject(file):
    try:
        n = struct.unpack("I", file.read(4))[0]
    except struct.error:
        return None
    print n
    return marshal.loads(file.read(n))

class Worker(threading.Thread):
    def run(self):
        # we could save some overhead by forking, but this is more
        # portable
        process = subprocess.Popen(
            executable + [sys.argv[0], "--process"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE
            )
        stdin = process.stdin
        stdout = process.stdout
        while 1:
            cmd = queue.get()
            if cmd is None:
                stdin.write("0\n")
                break
            print cmd
            print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
            putobject(stdin, cmd)
            getobject(stdout)
            queue.task_done()

# --------------------------------------------------------------------

import time, sys



if "--process" in sys.argv:

    stdin = sys.stdin
    stdout = sys.stdout
    while 1:
        args = getobject(stdin)
        if args is None:
            sys.exit(0) # terminate
        process(*args)
        putobject(stdout, result)

else:

    FILE = "Maestra.csv"

    queue = Queue.Queue()

    # fire up a bunch of workers (typically one per core)
    for i in range(CPUS):
        w = Worker()
        w.setDaemon(1)
        w.start()

    chunksize = 1 # megabyte

    # distribute the chunks
    for chunk in getchunks(FILE, chunksize*1024*10):
        queue.put((FILE, chunk))

    # wait for the tasks to finish
    queue.join()



