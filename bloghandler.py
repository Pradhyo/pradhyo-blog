from handler import Handler
from google.appengine.ext import db

class BlogHandler(Handler):
	def get(self):
		"""Render BlogHome.html and pass all posts to it- recent first"""
		posts = Post.all().order('-created')
		self.render("BlogHome.html", posts = posts)


def blog_key(topic = 'non-tech'):
	"""Assign blog key with parent as topic """
	return db.Key.from_path('blogs', topic)

class Post(db.Model):
	"""Defines each blog post """
	title = db.StringProperty(required = True)
	blog = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	edited = db.DateTimeProperty(auto_now = True)

class NewPost(Handler):
	def get(self):
		"""Show page where a new post can be submitted """
		self.render("NewPost.html")

	def post(self):
		"""Get title and blog and store new Post entry with those values"""
		title = self.request.get('title')
		blog = self.request.get('blog')
		topic = self.request.get('topic')

		if title and blog:
			temp_post = Post(parent = blog_key(topic = topic), title = title, post = post)
			temp_post.put()
			self.redirect('/blog')
		else: 
			error = "Enter both :/"
			self.render("NewPost.html", title = title, blog = blog, error = error)








