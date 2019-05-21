"""
Parts:
- Tally all the char counts
- Turn the char counts into an array of trees to be combined
- Consolidate the trees using huffman procedure
"""
def huffman(text):
	"""Takes a string and returns a
	tree corresponding to the optimal huffman encoding."""
	def char_freqs(text):
		"""Takes a string and returns a dictionary of frequencies."""
		chars = list(text)
		freqs = {}
		for char in chars:
			if char in freqs:
				freqs[char] += 1
			else:
				freqs[char] = 1
		return freqs

	def make_tree_dict(freqs):
		"""Returns a dictionary of chars mapped to leaf nodes."""
		res = {}
		for char, freq in freqs.items():
			res[char] = Tree(char, None)
		return res

	def consolidate(freqs, trees):
		"""Destructively merges the 2 miniminal frequency trees."""
		first_min, first_freq = get_min(freqs)
		second_min, second_freq = get_min(freqs)
		first_tree, second_tree = trees.pop(first_min), trees.pop(second_min)
		merged_key = first_min + " " + second_min
		freqs[merged_key] = first_freq + second_freq
		trees[merged_key] = Tree(merged_key, [first_tree, second_tree])	

	def get_min(freqs):
		"""Returns and removes the lowest frequency key."""
		low = list(freqs)[0]
		for char, freq in freqs.items():
			if freq < freqs[low]:
				low = char
		low_freq = freqs.pop(low)
		return low, low_freq

	freqs = char_freqs(text)
	trees = make_tree_dict(freqs)
	while (len(trees) > 1):
		#iterates while we don't have a complete huffman tree
		consolidate(freqs, trees)
	return trees[list(trees)[0]]

class Tree:
	def __init__(self, char, branches):
		self.char = char
		if branches:
			self.left = branches[0] #0 bit
			self.right = branches[1] #1 bit
		else:
			self.left = None
			self.right = None
	
	def is_leaf(self):
		return self.left == None and self.right == None