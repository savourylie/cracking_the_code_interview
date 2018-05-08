def URLify(string, length):
	if not string:
		return string

	return ''.join([string[i] if string[i] != ' ' else '%20' for i in range(length)])

if __name__ == '__main__':
	assert URLify("Mr John Smith", 13) == "Mr%20John%20Smith"
	assert URLify("", 0) == ""
	assert URLify(" ", 1) == "%20"
	assert URLify("MrJohnSmith", 11) == "MrJohnSmith"
	print("All tests passed.")