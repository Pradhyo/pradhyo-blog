from handler import Handler, render_str
from google.appengine.ext import db

class BlogHandler(Handler):
	def get(self):
		"""Render BlogHome.html and pass all posts to it- recent first"""
		posts = Post.all().order('-created')
		category = self.request.get('category')
		if category:
			posts.ancestor(blog_key(category = category))
		self.render("BlogHome.html", posts = posts, search = True)

def blog_key(category = 'non-tech'):
	"""Assign blog key with parent as category """
	return db.Key.from_path('blogs', category)

class Post(db.Model):
	"""Defines each blog post """
	title = db.StringProperty(required = True)
	blog = db.TextProperty(required = True)
	created = db.DateTimeProperty(auto_now_add = True)
	edited = db.DateTimeProperty(auto_now = True)

	def render_post(self):
		"""Return this post properly with title and blog showing properly """
		#Since we are passing as html, convert new lines to <br> to render new lines properly
		self._render_text = self.blog.replace('\n', '<br>')
		return render_str("post.html", p = self)

class NewPost(Handler):
	def get(self):
		"""Show page where a new post can be submitted """
		self.render("NewPost.html")

	def post(self):
		"""Get title and blog and store new Post entry with those values"""
		title = self.request.get('title')
		blog = self.request.get('blog')
		category = self.request.get('category')

		if title and blog:
			if not category:
				category = 'non-tech'
			temp_post = Post(parent = blog_key(category = category), title = title, blog = blog)
			temp_post.put()
			self.redirect('/blog')
		else: 
			error = "Enter both :/"
			self.render("NewPost.html", title = title, blog = blog, error = error)