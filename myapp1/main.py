# Copyright 2016 Google Inc.
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

import webapp2
import cgi

form = """
<form method="post">
     What is your birthday?
     <br>
     <label>Month
        <input type="text" name="month" value="%(month)s">
     </label>
     <label>Day
        <input type="text" name="day" value="%(day)s">
     </label>
     <label>Year
        <input type="text" name="year" value="%(year)s">
     </label>
     <div style="color:red">%(error)s</div>
     <br>
     <br>	
     <input type="submit">
</form>
"""

def escape_html(s):
	return cgi.escape(s, quote=True)

def valid_day(day):
	if day and day.isdigit():
		day = int(day)
		if day>0 and day<=31:
		 	return day

def valid_year(year):
	if year and year.isdigit():
		year = int(year)
		if year>1900 and year<2020:
			return year

months = ['January', 'February', 'March', 'April','May','June','July','August','September','October','Novement','December']
def valid_month(month):
        monabb = dict( (m[:3].lower(),m) for m in months )
	if month:
           short_month = month[:3].lower()
           return monabb.get(short_month)
 
class MainPage(webapp2.RequestHandler):
    def write_form(self,error="", month="",day="",year=""):
        self.response.out.write(form % {"error":error, 
                                        "month": escape_html(month),
                                        "day": escape_html(day),
                                        "year": escape_html(year) })

    def get(self):
        #self.response.headers['Content-Type'] = 'text/plain'
        self.write_form()
    def post(self):
        user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')
        
        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year) # debug for long time could not know why 1982 is not valid, because I call valid_day(). 

        if not (month and day and year):
             self.write_form("That's not a valid one!",user_month,user_day,user_year)
        else:
             self.redirect("/thanks")

class ThanksHandler(webapp2.RequestHandler):
	def get(self):
		self.response.out.write("Thanks! It's valid birthday!")

class TestHandler(webapp2.RequestHandler):
    def post(self):
        q = self.request.get("q")
        self.response.out.write(q)
        
        #self.response.headers['Content-Type'] = 'text/plain'
        #self.response.out.write(self.request)

app = webapp2.WSGIApplication([('/',MainPage), ('/thanks',ThanksHandler) ],
				debug=True)
