import numpy
import math

x = [[1,2,2], [1,0], [1,0]]
w = [[0.5,0.5,0.5], [0.5, 0.5], [0.5,0.5]]
y = [3, 1]
out = [0, 0, 0]
nu = 0.5

def act(net):
	out = (1 - math.e ** (-net))/(1 + math.e ** (-net))
	if out >= 0.5:
		return 1
	elif out < 0.5:
		return 0

def v_out(x, w):
    for n in range(len(x)):
        net = numpy.dot(x[n], w[n])
        print(net)
        out[n] = act(net)
        print(out[n])
        

def print_out():
    for i in range (len(out)):
	    print(out[i])
	    
#print_out()
v_out(x, w)
        
