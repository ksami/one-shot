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
import jinja2
import os

# set jinja to be able to read from directory no matter where on the hard disk
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainPage(webapp2.RequestHandler):
	# if someone tries to get me, i render the template called ... .hmtl
    def get(self):
    	template = jinja_environment.get_template('main.html')
      	self.response.out.write(template.render())
        # self.response.write('Hello world!')

# if url ends with just / run the class MainPage
app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)