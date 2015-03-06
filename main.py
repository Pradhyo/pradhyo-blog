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

welcome = """ <b> Welcome to Pradhyo's blog </b>
<br>
This is a testbed for me to learn web development. 
<br>
Choose from what I have built so far:

<form>
	<select name='project'>
		<option value = "1">Rot13</option>
		<option value = "Soon">Coming Soon</option>
	</select>
	<input type = "submit">

</form> """

rot13form = """ <b> Enter some text to ROT13: </b>
<br>
<br>

<form>
<textarea name = "string"> Enter text here.. </textarea>
<br>

<input type = "submit">
</form> """

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	self.response.headers['Content-Type'] = 'text/html'
        self.response.write(welcome)

	def post(self):
		if self.request.get('project'):
			self.response.write("You wrote Rot13")


class Rot13Handler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.response.write(rot13form)

app = webapp2.WSGIApplication([('/', MainHandler),
								('/rot13', Rot13Handler)], debug=True)
