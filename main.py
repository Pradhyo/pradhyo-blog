import webapp2
from mainhandler import MainHandler
from misc_handler import Rot13Handler, ImgResize
from bloghandler import BlogHandler, NewPost, PostPage
from handler import Handler, render_str
from google.appengine.ext import db

class Transaction(db.Model):
	amount = db.IntegerProperty()
	userid = db.IntegerProperty()

class TransactionHandler(Handler):
	def get(self):
		transactions = Transaction.all()
		self.render("Transactions.html", transactions = transactions)

	def post(self):
		try:
			amount = int(self.request.get('amount'))
			userid = int(self.request.get('userid'))
			temp_transaction = Transaction(amount=amount, userid=userid)
			temp_transaction.put()
			self.render("Transactions.html", transactions = [temp_transaction])
		except:
			self.response.write('{"status": "error", "data": null, "message": "Invalid parameters"}')

app = webapp2.WSGIApplication([('/', MainHandler),
							   ('/blog', BlogHandler),
							   ('/newpost', NewPost),
                               ('/blog/([a-z]+)/([0-9]+)', PostPage),
                               ('/resizer', ImgResize),
							   ('/rot13', Rot13Handler),
							   ('/api/transaction', TransactionHandler)], debug=True)
