import random
# This function performs modulo on x and y
def our_mod(x,y):
	z = x % y
	#print("z is", z)
	return (z,x,y)

def main():
	#print("I'm in main!")
	m,n,o = our_mod(10,4)
	#print("m is", m)
	#print(m,n,o)

	x = "help me"
	#print(x[4])
	#print(x[2:4])
	#print(x[2:4:2])
	#print(x[3:len(x)])
	#print(x[len(x)-2])
	#print(len(x))
	#print(x[-2])
	#print(x[0])
	#print(x[-7])
	#print(x[len(x)-7])
	#print(x + x)
	#print(x * 5)
	#print(x - x)
	#print("f" in "foo")
	#print("z" not in "foo")

	x = 0
	### The following two loops do the same thing
	while(x < 5):
		#print(x < 5)
		print(x)
		x = x + 1

	for foo in range(0, 5):
		print(foo)

	y = True

	### A for loop can't do this
	while(y == True):
		n = random.random()
		n = n * 100
		n = int(n)
		#n = n - (n % 1)
		#n = n // 1

		#print(n)
		if(n == 5):
			y = False



	print("out of loop")



if __name__ == '__main__':
	main()