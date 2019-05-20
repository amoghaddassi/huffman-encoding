"""
Parts:
- Tally all the word counts
- Turn the word counts into an array of trees to be combined
- Consolidate the trees using huffman procedure
"""
def huffman(text):
	"""Takes a string and returns a
	tree corresponding to the optimal huffman encoding."""
	def word_freqs(text):
		"""Takes a string and returns a dictionary of frequencies."""
		words = text.split(" ")
		freqs = {}
		for word in words:
			if word in freqs:
				freqs[word] += 1
			else:
				freqs[word] = 1
		return freqs

	def make_tree_dict(freqs):
		"""Returns a dictionary of words mapped to leaf nodes."""
		res = {}
		for word, freq in freqs.items():
			res[word] = Tree(word, None)
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
		for word, freq in freqs.items():
			if freq < freqs[low]:
				low = word
		low_freq = freqs.pop(low)
		return low, low_freq

	freqs = word_freqs(text)
	trees = make_tree_dict(freqs)
	while (len(trees) > 1):
		#iterates while we don't have a complete huffman tree
		consolidate(freqs, trees)
	return trees[list(trees)[0]]

class Tree:
	def __init__(self, word, branches):
		self.word = word
		if branches:
			self.left = branches[0] #0 bit
			self.right = branches[1] #1 bit
		else:
			self.left = None
			self.right = None
	
	def is_leaf(self):
		return self.left == None and self.right == None