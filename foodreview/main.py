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
import urllib
import webapp2
import jinja2
import os
import datetime

from google.appengine.ext import db
from google.appengine.ext import blobstore

# set jinja to be able to read from directory no matter where on the hard disk
jinja_environment = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainPage(webapp2.RequestHandler):
	# if someone tries to get me, i render the template called ... .hmtl
  def get(self):
	template = jinja_environment.get_template('main.html')
	self.response.out.write(template.render())
		# self.response.write('Hello world!')

class Stalls(db.Model):
  """Models an item with name as key name, description and date."""
  name = db.StringProperty()
  description = db.StringProperty(multiline=True)
  date = db.DateTimeProperty(auto_now_add=True)
  photo = db.StringProperty()

class Reviews(db.Model):
  """Models a review with username, userid, name of stall, review and date"""
  username = db.StringProperty()
  userid = db.IntegerProperty()
  stallname = db.StringProperty()
  text = db.StringProperty(multiline=True)
  photo = db.StringProperty()
  date = db.DateTimeProperty(auto_now_add=True)

class AddList(webapp2.RequestHandler):
  """ Add an item to the datastore """
  def get(self):
	query = db.GqlQuery("SELECT * FROM Stalls ORDER BY date DESC")
	template_values = {
		'stalls' : query,
		'string' : "Hello World!"
	}
	template = jinja_environment.get_template('add.html')
	self.response.out.write(template.render(template_values))

  def post(self):
	if(self.request.get('stall_name') != "" and self.request.get('stall_desc') != ""):
		stall = Stalls(key_name=self.request.get('stall_name'))
		#changes the time to GMT+8
		stall.name = self.request.get('stall_name')
		stall.description = self.request.get('stall_desc')
		stall.date = stall.date.replace(hour=(stall.date.hour+8)%24)
		stall.photo = self.request.get('stall_photo')


		######  Get username in string and userid in int here   #####
		#stall.userid = self.request.get('user_id')
		#stall.username=self.request.get('user_name')






		#stall.photo = db.Blob(open(self.request.get('stall_photo'),"rb").read())
		#img = images.resize(self.request.get('stall_photo'),200, 200)
		#stall.photo=db.Blob(img)  # bypass here. cannot use str.
		if stall.photo.rstrip() != '':
			stall.put()
	self.redirect('/search')

class Searchf(webapp2.RequestHandler):
	# if someone tries to get me, i render the template called ... .hmtl
  def get(self):
	query = db.GqlQuery("SELECT * FROM Stalls ORDER by date DESC Limit 30")
	template_values = {
		'stalls' : query,
		'string' : "Hello World!"
	}
	template = jinja_environment.get_template('search.html')
	self.response.out.write(template.render(template_values))

  def post(self):
	query = db.GqlQuery("SELECT * FROM Stalls ORDER BY date DESC")
	searchstring = self.request.get('stall_name_search')
	searchresult = []
	for x in query:
	 	if ( searchstring in x.name ):
	 		stall = Stalls()
	 		#changes the time to GMT+8
	 		stall.name = x.name
	 		stall.description = x.description
	 		stall.date = x.date
			stall.photo = x.photo
	 		searchresult.append(stall)
	template_values = {
		'stalls' : searchresult,
		'string' : "Hello World!"
	}
	template = jinja_environment.get_template('search.html')
	self.response.out.write(template.render(template_values))

class DisplayStalls(webapp2.RequestHandler):
	# if someone tries to get me, i render the template called ... .hmtl
  def get(self):
	title = self.request.query_string
	title = title.replace("%20", " ")
	query = Stalls.get_by_key_name(title)
	template_values = {
		'stall' : query,
		'string' : "Hellooooo",
		'search' : title
	}
	template = jinja_environment.get_template('display.html')
	self.response.out.write(template.render(template_values))

class AddReview(webapp2.RequestHandler):

  def get(self):
	#if self.request.get('user_name') != "":
	template_values = {'string' : 'Hello World!'}
	template = jinja_environment.get_template('addreview.html')
	self.response.out.write(template.render(template_values))
	#else:
	#	self.redirect(self.request.host_url)

  def post(self):
  	if (self.request.get('user_id') != None and self.request.get('user_name') != "" and self.request.get('userreview') != ""):
  		review = Reviews()
		review.userid = int(self.request.get('user_id'))
		review.username = self.request.get('user_name')
		review.text = self.request.get('review_text')
		review.date = review.date.replace(hour=(review.date.hour+8)%24)
		review.photo = self.request.get('review_photo')
		review.stallname = self.request.get('stall_name')
		review.put()
	self.redirect('/reviews')
	#self.redirect(self.request.host_url)

class DisplayReviews(webapp2.RequestHandler):

  def get(self):
	query = db.GqlQuery("SELECT * FROM Reviews ")
	template_values = {
		'reviews' : query,
		'string' : 'Hello World!'
	}
	template = jinja_environment.get_template('reviews.html')
	self.response.out.write(template.render(template_values)) 


# if url ends with just / run the class MainPage
app = webapp2.WSGIApplication([
	('/', MainPage),
	('/search', Searchf),
    ('/display.*', DisplayStalls),
    ('/addlist', AddList),
    ('/addreview', AddReview),
    ('/reviews', DisplayReviews)
], debug=True)
