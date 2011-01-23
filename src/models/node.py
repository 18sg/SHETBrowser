from PyQt4.QtGui import QIcon

class SHETNode(object):
	"""
	A SHET node class represents all SHET nodes in the QAbstractModel.
	It is used to build the tree view.
	"""
	def __init__(self, node_name, parent):
		#Set the parent, name and node type.
		self._parent = parent
		self._node_name = node_name
		
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
		return None
	def get_icon(self):
		"""
		Return the icon for this node type.
		"""
		return QIcon()

class SHETDirNode(SHETNode):
	def data(self, column):
		if column == 0:
			return self._node_name
		elif column == 1:
			return "Directory"
		else:
			return None
	def get_icon(self):
		return QIcon("folder.png")

class SHETEventNode(SHETNode):
	def data(self, column):
		if column == 0:
			return self._node_name
		elif column == 1:
			return "Event"
		else:
			return None
	def get_icon(self):
		return QIcon("event.png")

class SHETActionNode(SHETNode):
	def data(self, column):
		if column == 0:
			return self._node_name
		elif column == 1:
			return "Action"
		else:
			return None
	def get_icon(self):
		return QIcon("action.png")

class SHETPropertyNode(SHETNode):
	def data(self, column):
		if column == 0:
			return self._node_name
		elif column == 1:
			return "Property"
		else:
			return None
	def get_icon(self):
		return QIcon("property.png")

"""
Define a dict for mapping SHET string node types to
SHETNode subclass types.
"""
NodeMap = {'action' : SHETActionNode, 
           'event' : SHETEventNode,
           'prop' : SHETPropertyNode}

