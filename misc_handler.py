from handler import Handler
import codecs
from google.appengine.api import images

def resize_image(img, max_width, max_height, crop = False):
	"""Returns resized image not exceeding max_size while maintaining
	aspect ratio """
	width, height = img.size
	if crop:
		factor = max(max_width/float(width), max_height/float(height))
	else:
		factor = min(max_width/float(width), max_height/float(height))
	return img.resize((int(width*factor),int(height*factor)), images.ANTIALIAS)

class Rot13Handler(Handler):
	
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("rot13.html", text = "Enter text..")

	def post(self):
		string = self.request.get("text")
		string = codecs.encode(string,'rot13')
		self.response.headers['Content-Type'] = 'text/html'
		self.render("rot13.html", text = string)

class ImgResize(Handler):
	"""Handler for resizing images"""
	def get(self):
		self.render("img_resize.html")

	def post(self):
		img = self.request.get('img')
		max_width = self.request.get('max_width')
		max_height = self.request.get('max_height')
		self.render("img_resize.html", img = img, height = max_height, width = max_width)
		
