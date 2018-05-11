from linkedlist import Node, create_linkedlist, linkedlist_equal, print_linkedlist

def sum_lists(ll1, ll2, reverse=True):
	if reverse:
		head1 = ll1
		head2 = ll2
		current1 = head1
		current2 = head2
		carry = 0
		prev = None

		while current1 is not None:
			if current2 is not None:
				sm = current1.value + current2.value + carry
				carry, current1.value = sm // 10, sm % 10
				prev = current1
				current1, current2 = current1.next, current2.next

		while current2 is not None:
			prev.next = Node()
			current1 = prev.next
			current1.value = current2.value + carry
			prev = current2
			current2 = current2.next

		if carry != 0:
			prev.next = Node()
			prev.next.value = carry

		return head1

	else:
		ll1_str = ''
		ll2_str = ''

		while ll1 is not None:
			ll1_str += str(ll1.value)
			ll1 = ll1.next
		while ll2 is not None:
			ll2_str += str(ll2.value)
			ll2 = ll2.next

		result_str = str(int(ll1_str) + int(ll2_str))

		return create_linkedlist(result_str)


if __name__ == '__main__':
	ll1r = create_linkedlist([7, 1, 6])
	ll2r = create_linkedlist([5, 9, 2])

	print("ll1")
	print_linkedlist(ll1r)
	print("ll2")
	print_linkedlist(ll2r)
	print("sum")
	print_linkedlist(sum_lists(ll1r, ll2r))

	ll1 = create_linkedlist([7, 1, 6][::-1])
	ll2 = create_linkedlist([5, 9, 2][::-1])

	print("ll1")
	print_linkedlist(ll1)
	print("ll2")
	print_linkedlist(ll2)
	print("sum")
	print_linkedlist(sum_lists(ll1, ll2, reverse=False))


