import os


def tree(path):
	"""
	Open output text document with context manager and execute file tree generation within it.
	:param path: full Windows-style path to directory of interest
	"""
	original_depth = len(path.split('\\'))
	print()
	traverse(path, original_depth)
	print()


def traverse(path, original_depth):
	"""
	List all contents of a directory and recursively traverse the subdirectories.
	:param path: full Windows-style path to directory of interest
	:param original_depth: the depth of the original directory for which this program was called
	:param doc: the text document to be written to
	"""
	# list all directories within current path
	contents = os.listdir(path)
	
	# iterate over list of contents
	for item in contents:
		
		# if item is a file (not a directory)
		if '.' in item:
			# locate full path of item	
			for root, dirs, files in os.walk(path):
				for name in files:
					append(path, original_depth, root, name, item)
		
		# if item is a directory (not a file)
		else:
			# locate full path of item
			for root, dirs, files in os.walk(path):
				for name in dirs:
					append(path, original_depth, root, name, item)

			# continue recursively searching the current directory
			traverse(str(os.path.join(path, item)), original_depth)


def append(path, original_depth, root, name, item):
	"""
	Write directory or file name to text document with appropriate indentation.
	:param path: full Windows-style path to directory of interest
	:param original_depth: the depth of the original directory for which this program was called
	:param doc: the text document to be written to
	:param root: 
	:param name: 
	:param item: 
	"""
	if name == item:
		x = os.path.abspath(os.path.join(root, name))
		# determine how 'deep' item is within the file hierarchy w.r.t the original directory
		curr_depth = len(path.split('\\')) - original_depth
		
		# format the file name based on its 'depth'
		print(('\t' * curr_depth) + item)
