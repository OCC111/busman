import time
def fib():
	a,b = 0,1
	for i in range(10):
		yield a,b
		a,b = b,a+b
def fib1():
	a,b = 0,1
	for i in range(10):
		yield a,b
		a,b = b,a+b


while True:
	G = fib()
	G1 = fib1()
	time.sleep(1)
