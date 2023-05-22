import time
length = 100000
start_time = time.time()
line = ''
for i in range(length):

    line = str(bin(i))
    print(line)
print ("This program took", time.time() - start_time, "seconds to count to", length, "in binary")
    