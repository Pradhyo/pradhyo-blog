from handler import Handler

class MainHandler(Handler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("HomePage.html")

	def post(self):
		if self.request.get("project") == "rot13":
			self.redirect("/rot13")
		else:
			self.response.write("I am still working on some cool stuff :)")