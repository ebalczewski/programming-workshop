# A) Find 4 reasons this function will fail
def add(x, y):

	sum_xy = x + y

	return(sum_xy)

# B) How do you represent this function in mathematical notation? What does it do?
def mystery_func(x, y):

	if y==0:
		return(1)
	else:
		return(x * mystery_func(x, y-1))

def main():
	# C) Will this print? True/False
	print("I'm in main")

	# D) What will the output of this be?
	print(type(1.5))

	# E) What will the output of this be?
	my_list = range(1,4)
	print(my_list[3])

	# F) What will the output of this be?
	for i in range(1,3):
		for j in range(2,4):
			print(i * i)

if __name__ == '__main__':
	main()