def factorial(n):

	#base cases
	if n==0:
		return(1)
	elif int(n)!= n:
		print("Not an integer, you numbskull")
		return(None)
	elif n<0:
		print("No factorials of negative numbers, you silly")
		return(None)
	elif n==1:
		return(1)
	else:
		#recursive function call
		print("n is ", n)
		print(n*factorial(n-1))
		return(n*factorial(n-1))

def main():
	#print(factorial(5))
	print(factorial(0))
	print(factorial(3.5))
	print(factorial(4))
	#print(factorial(997))

if __name__ == '__main__':
	main()