class Node:

	def __init__(self, data):

		self.data = data
		self.next = None
	def __str__(self):

		return str(self.data)

class Link_list:

	def __init__(self):
		self.head = None
		self.tail = None

	def is_empty(self):

		return self.head is None

	def append(self, data):
		node = Node(data)
		if self.head is None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node
	def iter(self):
		if self.head is 	None:
			return ''
		else:
			cur = self.head
			yield cur.data
			while cur.next :
				cur = cur.next
				yield cur.data
	def insert(self, id, data):

		cur = self.head
		cur_id = 0
		if cur is None:
			raise Exception('this list is empty')
		while cur_id < id-1:
			cur = cur.next
			if cur_id is None:
				raise Exception('list length less than index')
			cur_id += 1
		node = Node(data)
		node.next = cur.next
		cur.next = node
		if node.next is None:
			self.tail = node

	def remove(self, id):
		cur = self.head
		cur_id = 0
		if cur.head is None:
			raise Exception('empty')
		while cur_id < id-1:
			cur = cur.next
			if cur is None:
				raise Exception('than index')
			cur_id += 1
		if id ==0:
			head = cur.next
			cur = cur.next
			return 
		if self.head == self.tail:
			self.head = None
			self.tail = None
			return
		cur.next = cur.next.next
		if cur.next is None:
			self.tail = cur

	def size(self):
		current = self.head
		count = 0
		if self.head is None:
			raise Exception('empty')
		while current is not None:
			count += 1
			current = current.next

	def search(self, item):

		current = self.head
		found = False

		while current is not None and not found:
			if current.data == item:
				found = False
			else:
				current = current.next
		return found

	def reverse(self):
		#此处为考虑tail  0.0懒一下
		cur = self.head
		pre = None
		h =self.head

		if self.head is None or self.head.next is None:
			return self.head
		else:
			while cur:
				
				temp = cur.next
				cur.next = pre
				pre = cur
				cur = temp 
			self.tail = h
			self.head = pre

			return pre

	
node1 = Node(4)
# node2 = Node(3)
# node1.next = node2
# print(node1, node1.next)
link_list = Link_list()
link_list.head = node1
link_list.tail = node1
if not link_list.is_empty():
	print('kong')
link_list.append(3)
link_list.insert(1,2)
for i in link_list.iter():
	print(i)
l = link_list.reverse()
while l :
	print(l.data)
	l = l.next