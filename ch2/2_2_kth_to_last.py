from linkedlist import Node, create_linkedlist, linkedlist_equal, print_linkedlist

def kth_to_last_recursion(head, k):
	if head.value is None:
		return 0

	index = kth_to_last(head.next, k) + 1

	if index == k:
		print("{0}th element is {1}".format(k, head.value))

	return index

def kth_to_last(head, k):
	if head is None:
		raise ValueError("Linkedlist doesn't exist.")

	length = 0
	current = head

	while current is not None:
		current = current.next
		length += 1

	pos = length - k - 1
	current = head
	i = 0

	while current is not None:
		if i == pos:
			return current.value

		current = current.next
		i += 1
		
if __name__ == '__main__':
	ll = create_linkedlist([1, 2, 3, 5, 12, 4])

	print(kth_to_last(ll, 6))