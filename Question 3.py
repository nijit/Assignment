def reverseSting(text):
	index = -1

	# Loop from last index until half of the index	
	for i in range(len(text)-1, int(len(text)/2), -1):

		# match character is alphanumeric or not		
		if text[i].isalnum():
			temp = text[i]
			while True:
				index += 1
				if text[index].isalnum():
					text[i] = text[index]
					text[index] = temp
					break
	return text
	
# Driver code
string = input("Enter your string: ")
print ("Input string: ", string)
string = reverseSting(list(string))
print ("Output string: ", "".join(string))
