# Enforcing Privacy with Cryptography
# Author - Immanuel Kolapo
"""This contains three functions - encryptData(),
keyGenerator(), and decryptData() - that encrypts,
gets encryption keys and decrypts any four
digit integer supplied by the user.

Know that if the encryption function returns a 
three-digit integer, to decrypt it you have to
add a zero at the beginning of the digits to make
a four-digit integer.

Also know that if you're getting just a single digit
after decryption, then you can add three zeros at the
beginning to make a four-digit decrypted integer."""

# Encryption function
def encryptData(intData):
	if isinstance(intData, str):
		dataList = []
		swappedDataList = []

		if len(intData) == 4:
			for num in intData:
				value = int(num) + 7
				rem = value % 10
				remToStr = str(rem)
				dataList.append(remToStr)

			swappedDataList.insert(0, dataList[2])
			swappedDataList.insert(2, dataList[0])
			swappedDataList.insert(1, dataList[3])
			swappedDataList.insert(3, dataList[1])

			encryptedData = int(''.join(swappedDataList))
			print(encryptedData)
		else:
			print("ValueError: expected a four digit integer in string form, got", len(intData))
	else:
		print("TypeError: four digit integer in string form only")

# Encryption generator function
def keyGenerator(intData):
	if isinstance(intData, str):
		
		if len(intData) == 4: 
			for num in intData:
				value = int(num) + 7
				rem = value % 10
				k = (value - rem) / 10
				decryptKey = (int(k), 10)
				print(decryptKey)
		else:
			print("ValueError: expected a four digit integer in string form, got", len(intData))
	else:
		print("TypeError: four digit integer in string form only")

# Decryption function
def decryptData(intData):
	if isinstance(intData, str):
		dataList = list(intData)
		swappedDataList = []
		decryptedDataList = []

		if len(intData) == 4: 
			swappedDataList.insert(0, dataList[2])
			swappedDataList.insert(2, dataList[0])
			swappedDataList.insert(1, dataList[3])
			swappedDataList.insert(3, dataList[1])
			
			swappedEncryptedData = int(''.join(swappedDataList))
			print(swappedEncryptedData)
			swappedEncryptedDataToStr = str(swappedEncryptedData)

			for num in swappedEncryptedDataToStr: 
				k = int(input("First key value in tuple: "))
				c = int(input("Second key value in tuple: "))
				print("")				
				for count in range(4):
					b = (k * c) + int(num)
					decryptedValue = b - 7
				decryptedValueToStr = str(decryptedValue)
				decryptedDataList.append(decryptedValueToStr)

			decryptedData = int(''.join(decryptedDataList))
			print(decryptedData)
		else:
			print("ValueError: expected a four digit integer in string form, got", len(intData))
	else:
		print("TypeError: four digit integer in string form only")

# Interactivity
print("\nEnforcing Cryptography")
print("\nPress 1 to Encrypt.\n\
Press 2 to get Encryption Keys.\n\
Press 3 to Decrypt")

prompt = ">>> "
try:
	functionCriteria = int(input(prompt))
	if functionCriteria == 1:
		print("\nFour digit integer to Encrypt")
		digitToEncrypt = str(input(prompt))
		encryptData(digitToEncrypt)
	elif functionCriteria == 2:
		print("\nFour digit integer to get Encryption Keys for")
		digitToGetEncryptKeys = str(input(prompt))
		keyGenerator(digitToGetEncryptKeys)
	elif functionCriteria == 3:
		print("\nFour digit integer to Decrypt")
		digitToDecrypt = str(input(prompt))
		decryptData(digitToDecrypt)
	else:
		print("InvalidInputError: expected 1, 2 or 3, got", functionCriteria)
except NameError as ne:
	print("NameError:", ne)
except ValueError as ve:
	print("ValueError:", ve)