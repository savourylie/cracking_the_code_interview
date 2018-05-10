class Node(object):
	def __init__(self):
		self.value = None
		self.next = None

def create_linkedlist(iterable):
	head = Node()
	current = head

	for i, x in enumerate(iterable):
		current.value = x
		current.next = Node()
		current = current.next

	return head

def print_linkedlist(ll):
	while ll is not None:
		print(ll.value)
		ll = ll.next


def linkedlist_equal(ll1, ll2):
	if ll1 is None and ll2 is None:
		return True

	while ll1 is not None:
		try:
			if ll1.value != ll2.value:
				return False
		except AttributeError:
			return False

		ll1 = ll1.next
		ll2 = ll2.next

	if ll2 is not None:
		return False

	return True



if __name__ == '__main__':
	ll1 = create_linkedlist([1, 2, 3, 4, 5, 6, 7])
	ll2 = create_linkedlist([1, 2, 3, 4, 5, 6])

	print(linkedlist_equal(ll1, ll2))



