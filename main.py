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
import os
import jinja2

class Rot13Handler(Handler):
	
	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("rot13.html", text = "Enter text..")

	def post(self):
		string = self.request.get("text")
		string = codecs.encode(string,'rot13')
		self.response.headers['Content-Type'] = 'text/html'
		self.render("rot13.html", text = string)

app = webapp2.WSGIApplication([('/', MainHandler),
								('/rot13', Rot13Handler)], debug=True)
