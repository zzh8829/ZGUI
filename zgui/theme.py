import zgui.guilocal as local
from .base import *

class Theme():
	"""Theme Class for handlling color theme"""

	DEFAULT = {
	
	}

	WINDOWS8GRAY = {
		'UIFONT': 'res/segoeui.ttf',
		'DIALOGBACKGROUND': (240,240,240),
		'BACKGROUND': GRAY,
		'WINDOWTITLEACTIVE': (151,151,151),
		'WINDOWTITLEINACTIVE': (235,235,235),
		'WINDOWBORDEROUTACTIVE': (115,115,115),
		'WINDOWBORDEROUTINACTIVE': (211,211,211),
		'WINDOWBORDERINACTIVE':  (128,128,128),
		'WINDOWBORDERININACTIVE': (218,218,218),
		'BUTTONUP' : (236,236,236),
		'BUTTONUPBORDER': (172,172,172),
		'BUTTONDOWN' : (203,228,252),
		'BUTTONDOWNBORDER' :(86,157,229),
		'BUTTONOVER' : (225,249,252),
		'BUTTONOVERBORDER':(126,180,234),
		'MENUBAR':(245,246,247),
		'MENUDOWN':(183,216,249),
		'MENUOVER':(183,216,249),
		'MENUDOWNBORDER' :(122,177,232),
		'MENUBORDER':(218,219,220),
		'POPMENUBACKGROUND': (240,240,240)

	}

	def __init__(self,**args):

		self.theme = self.DEFAULT
		if 'theme' in args and args['theme'] in dir(self):
			self.theme = getattr(self,args['theme'])

	def __getitem__(self,key):
		"""return color of theme"""
		return self.theme[key]



