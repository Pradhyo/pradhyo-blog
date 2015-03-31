from handler import Handler

class BlogHandler(Handler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("BlogHome.html")

def blog_key(topic = 'non-tech'):
	"""Assign blog key with parent as topic """
	return db.Key.from_path('blogs', topic)

class Post(db.Model):
	"""Defines each blog post """
	title = db.StringProperty(required = True)
	blog = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	edited = db.DateTimeProperty(auto_now = True)



