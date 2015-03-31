import webapp2
from mainhandler import MainHandler
from rot13handler import Rot13Handler
from bloghandler import BlogHandler, NewPost

app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/blog', BlogHandler),
							   ('/newpost', NewPost),
							   ('/rot13', Rot13Handler)], debug=True)
