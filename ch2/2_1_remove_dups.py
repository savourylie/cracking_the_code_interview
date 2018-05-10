from linkedlist import Node, create_linkedlist, linkedlist_equal, print_linkedlist
def remove_dups(ll):
	unique_set = set()
	head = ll
	prev = None

	while ll is not None:
		if ll.value not in unique_set:
			unique_set.add(ll.value)
			prev = ll
			ll = ll.next

		else:
			if ll.next is not None:
				prev.next = ll.next
				ll = ll.next
			else:
				prev.next = Node()
				ll = ll.next


	return head


if __name__ == '__main__':
	ll1 = create_linkedlist([1, 1, None, None, 3, 5, 2, 3, 4, 1, 5, 3, 1, 5, 2])
	ll2 = create_linkedlist([1, None, 3, 5, 2, 4])

	assert linkedlist_equal(remove_dups(ll1), ll2)
	print("All tests passed.")




