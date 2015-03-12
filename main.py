#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import codecs
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment (loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

rot13form = """ <b> Enter some text to ROT13: </b>
<br>
<br>

<form method=post>
<textarea name = "text">%s</textarea>
<br>

<input type = "submit">
</form> """

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self,template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class MainHandler(Handler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("Welcome.html")

	def post(self):
		if self.request.get("project") == "rot13":
			self.redirect("/rot13")
		else:
			self.response.write("I am still working on some cool stuff :)")


class Rot13Handler(Handler):
	
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(rot13form %"Enter text..")

	def post(self):
		string = self.request.get("text")
		string = codecs.encode(string,'rot13')
		string = cgi.escape(string)
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(rot13form %string)

app = webapp2.WSGIApplication([('/', MainHandler),
								('/rot13', Rot13Handler)], debug=True)
