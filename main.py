import webapp2
from mainhandler import MainHandler
from rot13handler import Rot13Handler

app = webapp2.WSGIApplication([('/', MainHandler),
								('/rot13', Rot13Handler)], debug=True)
