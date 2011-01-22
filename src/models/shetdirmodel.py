from PyQt4 import QtCore
from node import *

class SHETDirModel(QtCore.QAbstractItemModel):
	"""
	A subclass of the QAbstractModel that provides
	a tree-like dir read only model to a QTreeView.
	"""
	def __init__(self, parent, dir_info):
		"""
		Construct the model. dir_info should be the
		dict returned by calling "/meta/ls-r" on SHET.
		"""
		super(SHETDirModel, self).__init__()
		
		# Create the root node object.
		self._root_node = SHETDirNode('/', None)
		
		# Setup the directory tree structure.
		self.setup_model_data(self._root_node, dir_info)
	
	def setup_model_data(self, parent, levelInfo):
		"""
		Given the dictionary returned from ls-r Construct
		the shet directory tree.
		"""
		for name, value in levelInfo.iteritems():
			if isinstance(value, dict):
				currentNode = SHETDirNode(name, parent)
				self.setup_model_data(currentNode, value)
			else:
				currentNode = NodeMap[value](name, parent)
			if parent != None:
				parent.append_child(currentNode)
	
	def index(self, row, column, parent):
		"""
		Return a QModelIndex of a child given a parent, row
		and column.
		"""
		if not parent.isValid():
			parentItem = slef._root_node
		else:
			parentItem = parent.internalPointer()
		
		childItem = parentItem.row(row)
		return createIndex(row, column, childItem)
		
	def parent(self, child):
		if not child.isValid():
			return QtCore.QModelIndex()
		parentObject = child.internalPointer().parent()
		if parentItem == self._root_node:
			return QtCore.QModelIndex()
		return createIndex(parent.row(), 0, parentItem)
	
	def rowCount(self, index):
		if not index.isValid():
			return self._root_node.child_count()
		return index.internalPointer().child_count()
	
	def columnCount(self, index):
		return 2
	
	def data(self, index, role):
		if not index.isValid():
			return object
		if role != QtCore.Qt.DisplayRole:
			return object
		return index.internalPointer.data(index.column())
	
	def flags(self, index):
		if not index.isValid():
			return 0
		return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
