from handler import Handler

class BlogHandler(Handler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("BlogHome.html")
