from handler import Handler
import requests
import base64

class Vision(Handler):

	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("vision.html")

	def post(self):
		url = self.request.get("url")
		response = requests.get(url).content
		b = base64.b64encode(response)
		self.render("vision.html", output = b)