def pal_checker_recursive(my_string):

	if(my_string[0]==my_string[-1]):
		if (len(my_string)!=1):
			pal_checker_recursive(my_string[1:-1])
	else:
		return(False)

	return(True)

def pal_checker_loop(my_string):

	for i in range(1,len(my_string)):
		if my_string[i-1]!=my_string[-i]:
			return(False)

	return(True)

def pal_checker_reverse(my_string):

	for i in my_string:
		reverse_string = reverse_string + my_string[-i]

	return(my_string==reverse_string):
		return(True)

	return(False)

def main():
	print("I'm in main!")
	print(pal_checker_recursive("racecar"))
	print(pal_checker_loop("racecar"))
	print(pal_checker_loop("blue"))


if __name__ == '__main__':
	print("I'm in weird check!")
	main()