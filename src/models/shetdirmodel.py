from PyQt4 import QtCore
import node

class SHETDirModel(QtCore.QAbstractModel):
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
		self._root_node = SHETNode('/', NodeType.directory, None)
		self._shet_client = shet_client
		
		# Setup the directory tree structure.
		setup_model_data(self._root_node)
	
	def setup_model_data(self, parent, levelInfo):
		"""
		Given the dictionary returned from ls-r Construct
		the shet directory tree.
		"""
		for name, value in levelInfo.iteritems():
			if isinstance(value, dict):
				currentNode = SHETDirNode(name, parent)
				setup_model_data(currentNode, value)
			else
				currentNode = NodeMap[value](name, parent)
