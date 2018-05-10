from linkedlist import Node, create_linkedlist, linkedlist_equal, print_linkedlist

def del_mid_node(head, k):
	pos = 0
	current = head
	prev = None

	while current is not None:
		if pos == k:
			prev.next = current.next
			return head

		prev = current
		current = current.next
		pos += 1


if __name__ == '__main__':
	ll1 = create_linkedlist([1, 1, None, None, 3, 5, 2, 3, 4, 1, 5, 3, 1, 5, 2])
	ll2 = create_linkedlist([1, 1, None, 3, 5, 2, 3, 4, 1, 5, 3, 1, 5, 2])

	assert linkedlist_equal(del_mid_node(ll1, 2), ll2)

	print("All tests passed.")