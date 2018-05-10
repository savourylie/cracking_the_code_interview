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

def remove_dups_no_buffer(ll):
	head = ll
	p1, p2 = head, head.next
	prev = p1

	while p1 is not None:
		while p2 is not None:
			if p2.value == p1.value:
				prev.next = p2.next
				p2 = p2.next

			else:
				prev = p2
				p2 = p2.next
		
		p1 = p1.next

		try:
			p2 = p1.next
		except AttributeError:
			prev.next = Node()
			return head
		else:
			prev = p1

	return head


if __name__ == '__main__':
	ll1 = create_linkedlist([1, 1, None, None, 3, 5, 2, 3, 4, 1, 5, 3, 1, 5, 2])
	ll2 = create_linkedlist([1, None, 3, 5, 2, 4])

	assert linkedlist_equal(remove_dups(ll1), ll2)
	assert linkedlist_equal(remove_dups_no_buffer(ll1), ll2)
	
	print("All tests passed.")




