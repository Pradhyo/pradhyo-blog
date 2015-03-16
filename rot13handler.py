from handler import Handler
import codecs

class Rot13Handler(Handler):
	
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("rot13.html", text = "Enter text..")

	def post(self):
		string = self.request.get("text")
		string = codecs.encode(string,'rot13')
		self.response.headers['Content-Type'] = 'text/html'
		self.render("rot13.html", text = string)