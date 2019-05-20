"""Uses huffman.py to compress a given string."""
from huffman import *

def compress_text(text):
	huff_tree = huffman(text)
	bit_dict = {}
	bit_map(huff_tree, bit_dict, "")
	return process_bit_map(text, bit_dict)

def bit_map(huff_tree, out, curr_string):
	"""Takes a huff_tree and returns a bit map in the out dictionary.
	curr_string is the current bit string for our spot in the tree,
	makes recursion work nicely."""
	if (huff_tree.is_leaf()):
		out[huff_tree.word] = curr_string
		return None
	bit_map(huff_tree.left, out, curr_string + "0")
	bit_map(huff_tree.right, out, curr_string + "1")

def process_bit_map(text, bit_map):
	"""Takes a text with corresponding bit map and returns the string
	corresponding to the compressed text."""
	out = ""
	for word in text.split(" "):
		out += bit_map[word]
	return out
	