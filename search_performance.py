import random
import bisect
import matplotlib.pyplot as plt
import math
import time

def method_in(a,b,c):
    start_time = time.time()
    for i,x in enumerate(a):
        if x in b:
            c[i] = 1
    return(time.time()-start_time)   

def method_set_in(a,b,c):
    start_time = time.time()
    s = set(b)
    for i,x in enumerate(a):
        if x in s:
            c[i] = 1
    return(time.time()-start_time)

def method_bisect(a,b,c):
    start_time = time.time()
    b.sort()
    for i,x in enumerate(a):
        index = bisect.bisect_left(b,x)
        if index < len(a):
            if x == b[index]:
                c[i] = 1
    return(time.time()-start_time)

def profile():
    time_method_in = []
    time_method_set_in = []
    time_method_bisect = []

    Nls = [x for x in range(1000,20000,1000)] #generates values from 1000 to 20000 every 1000 values
    for N in Nls:
        # print("N=", N)
        a = [x for x in range(0,N)]           #fill the structures with a many values
        random.shuffle(a)
        b = [x for x in range(0,N)]
        random.shuffle(b)
        c = [0 for x in range(0,N)]

        time_method_in.append(math.log(method_in(a,b,c))) #To express the time in as a logarithm
        time_method_set_in.append(math.log(method_set_in(a,b,c)))
        time_method_bisect.append(math.log(method_bisect(a,b,c)))

#Instruction to build the graph
    plt.plot(Nls,time_method_in,marker='o',color='r',linestyle='-',label='in')
    plt.plot(Nls,time_method_set_in,marker='o',color='b',linestyle='-',label='set')
    plt.plot(Nls,time_method_bisect,marker='o',color='g',linestyle='-',label='bisect')
    plt.xlabel('list size', fontsize=18)
    plt.ylabel('log(time)', fontsize=18)
    plt.legend(loc = 'upper left')
    plt.show()
    
profile()
 

#################################
# enumerate() is a built-in function that allows us to loop over something
# and have an automatic counter. 
#
# For example: 
#     for counter, value in enumerate(some_list):
#         print(counter, value)
#
############################################
#
# From the graph generated, we can note that the search inside a set
# is faster when we have a lots of elements
#