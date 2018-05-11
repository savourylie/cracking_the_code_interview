from linkedlist import Node, create_linkedlist, linkedlist_equal, print_linkedlist


def palindrome(ll):
	if ll is None:
		return True

	result_str = ''

	while ll is not None:
		result_str += str(ll.value)
		ll = ll.next

	return result_str == result_str[::-1]


if __name__ == '__main__':
	ll1 = create_linkedlist([1, 2, 3, 2, 1])
	ll2 = create_linkedlist([1, 2, 3, 2, 1, 1, 1])
	ll3 = create_linkedlist([1, 2, 3, 3, 2, 1])

	assert palindrome(ll1)
	assert not palindrome(ll2)
	assert palindrome(ll3)

	print("All tests passed.")
