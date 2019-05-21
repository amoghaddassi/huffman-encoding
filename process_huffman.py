"""Uses huffman.py to compress a given string.
TODO: properly save the binary data to truly save space.
Right now just saving as text file so each bit is actually 
taking a byte of storage."""

from huffman import *

def compress_file(path, save = False, save_path = None):
	file = open(path, "r")
	text = file.read()
	return compress_text(text, save, save_path)

def compress_text(text, save = False, save_path = None):
	huff_tree = huffman(text)
	bit_dict = {}
	bit_map(huff_tree, bit_dict, "")
	res = process_bit_map(text, bit_dict)
	if save:
		file = open(save_path, "w")
		file.write(res)
		file.close()
	return process_bit_map(text, bit_dict)

def bit_map(huff_tree, out, curr_string):
	"""Takes a huff_tree and returns a bit map in the out dictionary.
	curr_string is the current bit string for our spot in the tree,
	makes recursion work nicely."""
	if (huff_tree.is_leaf()):
		out[huff_tree.char] = curr_string
		return None
	bit_map(huff_tree.left, out, curr_string + "0")
	bit_map(huff_tree.right, out, curr_string + "1")

def process_bit_map(text, bit_map):
	"""Takes a text with corresponding bit map and returns the string
	corresponding to the compressed text."""
	out = ""
	for char in list(text):
		out += bit_map[char]
	return out

def compression_ratio(original, compressed, bits_per_char_original = 8):
	"""Returns the compression ratio between the original text
	and the compressed text. Assumes compressed text is binary."""
	orig_bits = len(original) * bits_per_char_original
	comp_bits = len(compressed)
	return comp_bits / orig_bits