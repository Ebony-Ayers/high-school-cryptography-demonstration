def ceasarEncrypt(s, offset):
	output = ""
	for letter in s:
		#ingore all non letters
		if not letter.isalpha():
			output += letter
		else:
			#add the offset to the ascii value of the letter
			newAscii = ord(letter) + offset
			#calculate any letters that wrap around
			#because lowercase stays lowercase and upper case stays uppercase we need to handle the two seperatly
			if ord(letter) >= ord('a'):
				newAscii = ((newAscii - ord('a')) % 26) + ord('a')
			else:
				newAscii = ((newAscii - ord('A')) % 26) + ord('A')
			output += chr(newAscii)
	return output
def ceasarDecrypt(s, offset):
	#if encrypting is adding an offset then decryptinfg is simply subtracting the offset
	return ceasarEncrypt(s, -offset)

def main():
	mode = input("What do you want to do? Encrypt (e) or decrypt (d): ")
	while not (mode.lower() == 'e' or mode.lower() == 'd'):
		print("Your input must either be \'e\' or \'d\'. Please try again.\n")
		input("What do you want to do? Encrypt (e) or decrypt (d): ")
	
	if mode == 'e':
		message = input("Enter message to be encrypted: ")
	else:
		message = input("Enter message to be decrypted: ")
	
	offset = input("Enter the offset: ")
	while True:
		offset = int(offset)
		try:
			offset = int(offset)
			break
		except:
			print("Error the offset must be an integer. Please try again.\n")
			offset = input("Enter the offset: ")
	
	if mode == 'e':
		print(ceasarEncrypt(message, offset))
	else:
		print(ceasarDecrypt(message, offset))

if __name__ == "__main__":
	main()
