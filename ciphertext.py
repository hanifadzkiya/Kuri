def getPoint(char):
	# Determine if char is UpperCase or LowerCase
	# Return 65 if UpperCase and 97 if LowerCase
	if(ord(char) < 97):
		return 65
	else:
		return 97


def caesar_cipher(text,key):
	result = ""
	#Encrypt Process
	for idx in range(len(text)):
		point = getPoint(text[idx])
		if(text[idx] == " "):
			result = result + " "
		else:
			result = result + chr(((ord(text[idx])-point+key)%26) + point)
	return result

def vigenere_cipher(text,keyword):
	result = ""
	# Generate The Key
	key = ""
	repeat = (int)((len(text)-text.count(' ')) / len(keyword))
	for i in range(repeat):
		key = key + keyword
	remain = len(text) % len(keyword)
	for i in range(remain):
		key = key + keyword[i]
	# Encrypt Process
	tmp = 0
	for idx in range(len(text)):
		if(text[idx] == " "):
			result = result + " "
		else:
			pointText = getPoint(text[idx])
			pointKey = getPoint(key[tmp])
			result = result + chr(((ord(text[idx])-pointText+ord(key[tmp])-pointKey)%26) + pointText)
			tmp = tmp + 1
	return result