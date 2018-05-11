from linkedlist import Node, create_linkedlist, linkedlist_equal, print_linkedlist

def partition(ll, pivot):
	greater = []
	header = ll
	current  =  header
	prev = None

	while current.value is not None:
		if current.value >= pivot:
			greater.append(current.value)

			if prev is None:
				header = current.next
				current = header

			else:
				prev.next = current.next
				current = current.next

		else:
			prev = current
			current = current.next

	while greater:
		element = greater.pop(0)
		current.value = element
		current.next = Node()
		prev = current
		current = current.next

	return header


if __name__ == '__main__':
	lst = [3, 5, 8, 5, 10, 2, 1]
	ll = create_linkedlist(lst)
	pivot = 5

	print("List")
	print(lst)
	print("Linkedlist")
	print_linkedlist(ll)

	print("Linkedlist partitioned")
	ll_p = partition(ll, 5)
	print_linkedlist(ll)




