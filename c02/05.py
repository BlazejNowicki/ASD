def FindMajority(array):
	candidate = array[0]
	counter = 1
	for elem in array[1:]:
		if counter == 0:
			counter = 1
			candidate = elem
		else:
			if candidate == elem:
				counter += 1
			else:
				counter -= 1
	return candidate
