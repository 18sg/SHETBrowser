class NodeType:
	"""
	A simple enum type to identify the type of node.
	"""
	directory, event, action, prop = range(4)

class SHETNode:
	"""
	A SHET node class represents all SHET nodes in the QAbstractModel.
	It is used to build the tree view.
	"""
	def __init__(self, node_name, node_type, parent):
		#Set the parent, name and node type.
		self._parent = parent
		self._node_name = node_name
		self._node_type = node_type
		
		#initialise the children list
		self._children = list()
	
	def append_child(self, child):
		"""
		Append a child SHETNode object to this parent.
		"""
		self._children.append(child)
	
	def child(self, row):
		"""
		Return the child object for this row.
		"""
		return self._children[row]
	
	def parent(self):
		"""
		Return the parent for this object.
		"""
		return self._parent
	
	def child_count(self):
		"""
		Return the number of children for this object.
		"""
		return len(self._children)
	
	def row(self):
		"""
		Return the row number of this object in its parents
		child object list.
		"""
		if self._parent != None:
			return self._parent._children.index(self)
		else:
			return 0
	
	def data(self, column):
		"""
		Return either the name of the node or the type of the node.
		column = 0 Node name
		column = 1 Node type
		"""
		if column == 0:
			return self._node_name
		else if column == 1:
			return self._node_type
		else
			return None
