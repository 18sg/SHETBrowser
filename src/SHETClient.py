from shet.client import ShetClient

class SHETBrowserClient(ShetClient):
	"""
	This class provides Qt with an interface to SHET
	It allows the listing of directories calling actions,
	setting and getting properties and watching for events.
	"""
	def __init__(self):
		ShetClient.__init__(self)
	
	def list_dir(self, path):
		return self.call("/meta/ls", path)
