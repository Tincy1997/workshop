plainText = raw_input("What is your plaintext? ")
print plainText
shift = int(raw_input("What is your shift? "))
print shift

def caeser(plainText, shift):
	cipher = " "
	for ch in plainText:
		if ch.isalpha():
			ct = ord(ch) + shift
			if ct > ord('z'):
				ct -= 26
			cip = chr(ct)
			cipher += cip
	print "cipher text", cipher
	return cipher
caeser(plainText, shift)

