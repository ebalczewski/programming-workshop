
def factorial(n):

	if n==1:
		return(1)
	elif n==0:
		print("Factorial of 0 is 1, but it's actually the empty set, so...None")
		return(None)
	elif n<0:
		print("No factorials of negative numbers, silly")
		return(None)
	else:
		return(factorial(n-1) * n)

def main():
	print(factorial(-3))

if __name__ == '__main__':
	main()