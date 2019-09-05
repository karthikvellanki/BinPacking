from avltree import *
class Bin:
	def __init__(self):
		self.list = []

	def addItem(self, item):
		self.list.append(item)

	def removeItem(self, item):
		self.list.remove(item)

	def sum(self):
		total = 0
		for elem in self.list:
			total += elem
		return total

	def show(self):
		return self.list

def best_fit(list_items):
	""" Returns list of bins with input items inside. """
	list_bins = []
	list_bins.append(Bin()) # Add first empty bin to list
	bins = 0
	comparison = AVLTree()
	comparison.insert(1)

	index_capacity_pair = {}
	index_capacity_pair[1] = bins

	for item in list_items:
		# Go through bins and try to allocate
		alloc_flag = False
		k = item
		cur_node = comparison.root
		while cur_node != None:
			if cur_node.value < k:
				cur_node = cur_node.right_child
			elif cur_node.value > k:
				if cur_node.left_child != None and cur_node.left_child.value > k:
					cur_node = cur_node.left_child
				else:
					capacity = cur_node.value
					bin_index = index_capacity_pair[capacity]
					list_bins[bin_index].addItem(item)
					del index_capacity_pair[capacity]
					comparison.delete_value(capacity)
					new_capacity = 1 - list_bins[bin_index].sum()
					comparison.insert(new_capacity)
					index_capacity_pair[new_capacity] = bin_index
					alloc_flag = True 
					break

		if alloc_flag == False:
			newBin = Bin()
			bins = bins + 1
			newBin.addItem(item)
			list_bins.append(newBin)
			capacity = 1 - item
			comparison.insert(capacity)
			index_capacity_pair[capacity] = bins			
			
		# Turn bins into list of items and return
		# Turn bins into list of items and return
	result_items = []
	for bin in list_bins:
		result_items.append(bin.show())

	waste = len(list_bins) - sum(list_items)
	return waste
