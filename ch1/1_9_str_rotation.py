def str_rotation(s1, s2):
	return is_substring(s2 + s2, s1)

def is_substring(s1, s2):
	n = len(s1)
	m = len(s2)

	if m > n:
		return False

	if m == n and s1 != s2:
		return False

	for i in range(n - m + 1):
		if s1[i:i + m] == s2:
			return True

	return False

if __name__ == '__main__':
	s1 = 'waterfall'
	s2 = 'fallwater'

	assert str_rotation(s1, s2)
	