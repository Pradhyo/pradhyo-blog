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

welcome = """ <b> Welcome to Pradhyo's blog </b>
<br>
This is a testbed for me to learn web development. 
<br>
Choose from what I have built so far:

<form method = "post">
	<select name="project">
		<option value = "rot13">Rot13</option>
		<option value = "Soon">Coming Soon</option>
	</select>
	<input type = "submit">

</form> 
"""

rot13form = """ <b> Enter some text to ROT13: </b>
<br>
<br>

<form method=post>
<textarea name = "text">%s</textarea>
<br>

<input type = "submit">
</form> """

class MainHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(welcome)

	def post(self):
		if self.request.get("project") == "rot13":
			self.redirect("/rot13")
		else:
			self.response.write("I am still working on some cool stuff :)")


class Rot13Handler(webapp2.RequestHandler):
	
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
