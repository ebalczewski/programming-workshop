def main():
	# Don't name things "stuff"--not descriptive!
	stuff = [1,2,3]
	print(type(stuff))
	print(stuff)

	# We use append to add things to end of lists.
	stuff.append(4)
	print(stuff)

	# [] creates an empty list
	new_stuff = []
	for i in range(10,100,14):
		new_stuff.append(i)

	print(new_stuff)

	# Use a for loop to interate through lists!
	for i in range(len(new_stuff)):
		print(new_stuff[i])

	# You can also use a while loop :)
	j = 0
	while j < len(new_stuff):
		print(new_stuff[j])
		j+=1

	
	new_stuff.append(52)
	print(new_stuff)

	# What does remove do? (What if there are multiple of the thing you want to
	# remove in the list?)
	new_stuff.remove(52)
	print(new_stuff)

	# Sort of making our remove function...changes something to None.
	for i in range(len(new_stuff)):
		if new_stuff[i] == 52:
			new_stuff[i] = None

	print(new_stuff)

	# Use insert to add a value to a certain index.
	new_stuff.insert(5, "boo")
	print(new_stuff)

	# Lists of lists! Sort of like matrices.
	matrix = [[1,4,7],[2,5,8],[3,6,9]]
	matrix_2 = [[1,2,3],[4,5,6],[7,8,9]]

	# Iterating through each list to print out the numbers in numberical order.
	for i in range(len(matrix_2)):
		print(i)
		for j in range(len(matrix_2[i])):
			print(j)
			print("i is", i)
			print("j is", j)
			print(matrix_2[i][j])

	for i in range(matrix[j]):
		for j in range(3):
			print("i is", i)
			print("j is", j)
			print(matrix[j][i])


if __name__ == '__main__':
	main()