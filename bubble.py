def bubble(unsorted):

	length_unsorted = len(unsorted)
	
	#If we don't swap any numbers, the list is sorted.
	swaps = True
	while(swaps==True):
		swaps=False

		#Compare n=0 and n=1, then n=1 and n=2, ...
		for i in range(length_unsorted-1):
			if (unsorted[i] > unsorted [i+1]):
				#Swap two numbers, using a temp variable so we don't overwrite
				temp = unsorted[i+1]
				unsorted[i+1] = unsorted[i]
				unsorted[i] = temp
				swaps=True

		#We know the largest number will be at the end of the list
		#No point in continuing to check it!
		length_unsorted = length_unsorted-1

	return unsorted


def bubble_counter(unsorted):
	
	length_unsorted=len(unsorted)
	
	comparisons=0

	swaps=True
	while(swaps==True):
		swaps=False

		for i in range(length_unsorted-1):
			if (unsorted[i] > unsorted [i+1]):
				temp = unsorted[i+1]
				unsorted[i+1] = unsorted[i]
				unsorted[i] = temp
				swaps=True
				comparisons+=1

		length_unsorted = length_unsorted-1

	return(comparisons)


def main():

	unsorted = [5,4,3,2,1]
	sorted = bubble(unsorted)
	print(sorted)
	print(bubble_counter([5,4,3,2,1]))


if __name__ == '__main__':
	main()