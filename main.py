import webapp2
from mainhandler import MainHandler
from misc_handler import Rot13Handler, ImgResize
from bloghandler import BlogHandler, NewPost, PostPage

app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/blog', BlogHandler),
							   ('/newpost', NewPost),
                               ('/blog/([a-z]+)/([0-9]+)', PostPage),
                               ('/resizer', ImgResize),
							   ('/rot13', Rot13Handler)], debug=True)
