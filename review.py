def our_func(param1, param2):
	our_sum = param1 + param2
	#return(our_sum)

def main():
	print("I'm in main")
	#print(our_func(2,4))
	#other_func()
	x = 5
	y = "5"
	x = x + 1
	#print(x)
	y = y + "1"
	#print(y)

	#print(type(y))
	z = 3.14159

	# print(type(z))

	# print(type(None))

	# print(type(False))

	# print(int(z))
	# print(float(int(z)))
	# print(str(z))

	# print(bool(5))
	# print(int(round(3.6)))

	# print(10 % 9)

	# print(x != float(x))


	# if(False):
	# 	print("yay")

	# else:
	# 	print("bummer")

	# string = "help me"
	# print(string[2])
	# print(string[0:2])
	# print(string[-2])
	# print(len(string))
	# print(string[2:len(string)])
	# string_loong = string*10
	# print(string_loong)
	# print(string_loong[0:len(string_loong):3])
	# print("help" in string)
	x=1
	while(x < 5):
		print(x)
		x += 1

	for hey in range(1, 5):
		print(hey)


if __name__ == '__main__':
	main()