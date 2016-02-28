from handler import Handler
import requests
import base64

import argparse
import httplib2

from apiclient.discovery import build
from oauth2client.client import GoogleCredentials

class Vision(Handler):

	def get(self):
		self.response.headers['Content-Type'] = 'text/html'
		self.render("vision.html")

	def post(self):
		http = httplib2.Http()

		credentials = GoogleCredentials.get_application_default().create_scoped(['https://www.googleapis.com/auth/cloud-platform'])
		credentials.authorize(http)
		API_DISCOVERY_FILE = 'https://vision.googleapis.com/$discovery/rest?version=v1'
		service = build('vision', 'v1', http, discoveryServiceUrl=API_DISCOVERY_FILE)
		url = self.request.get("url")
		response = requests.get(url).content
		image_content = base64.b64encode(response)
		service_request = service.images().annotate(
		  body={
			'requests': [{
			  'image': {
				'content': image_content
			   },
			  'features': [{
				'type': 'LABEL_DETECTION',
				'maxResults': 5,
			   }]
			 }]
		  })
		response = service_request.execute()
		label = response['responses'][0]['labelAnnotations'][0]['description']
		# print('Found label: %s for %s' % (label, photo_file))
		# return 0
		self.render("vision.html", output = label)