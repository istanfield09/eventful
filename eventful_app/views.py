from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .models import Category

import simplejson
import objectpath
import json
import urllib2
import dateutil.parser
# Create your views here.

def show_cats(request):

	if request.method == 'GET':
		categories = Category.objects.all()

		return render(request, "eventful_app/home.html", {'categories': categories
					  })
	
def show_query(request, api_query):

	api_request = 'https://www.eventbriteapi.com/v3/events/search/?categories=' + api_query + '&token=6W6MK2IRTGDVSXQM3MNY'



	json_response = urllib2.urlopen(api_request)
	json_dat = json.load(json_response)

	outputs = json_dat['events']

	# Initialize arrays containing data for the events.
	name_array = []
	uri_array = []
	city_array = []
	region_array = []
	country_array = []
	date_array = []
	description_array = []

	# This array contains arrays of ticket data.
	ticket_data = []

	# Capture dictionary values of attributes of each entry in the list of events.
	for o in outputs:
		name = o["name"]["text"]
		url = o["organizer"]["url"]

		# Test if venue is NoneType. Collect location data.
		if o["venue"]:
			city = o["venue"]["address"]["city"]
			region = o["venue"]["address"]["region"]
			country = o["venue"]["address"]["country"]
		else:
			city = "N/A"
			region = "N/A"
			country = "N/A"

		# Collect start date data and make it (more) human readable.
		date_raw = dateutil.parser.parse(o["start"]["local"])
		date = date_raw.strftime("%a %B %d, %Y at %I:%M%p")

		# Test if event description exists. Collect event description.
		if o["description"]:
			description = o["description"]["text"]
		else:
			description = "N/A"

		# Collect information for each ticket class, and store
		# it in that event's ticket array.
		ticket_classes = o["ticket_classes"]

		ticket_names = []
		ticket_costs = []
		ticket_statuses = []

		for t in ticket_classes:	
			ticket_name = t["name"]

			if "cost" in t.keys():
				ticket_cost = t["cost"]["display"]
			else:
				ticket_cost = "Free"

			ticket_status = t["on_sale_status"]

			ticket_names.append(ticket_name)
			ticket_costs.append(ticket_cost)
			ticket_statuses.append(ticket_status)

		ticket_list = zip(ticket_names, ticket_costs, ticket_statuses)

		


		# Push all the data to their respective array.
		name_array.append(name)
		uri_array.append(url)

		city_array.append(city)
		region_array.append(region)
		country_array.append(country)

		date_array.append(date)

		description_array.append(description)

		ticket_data.append(ticket_list)


		

	# Zip the arrays into one big array.
	list = zip(name_array, uri_array, city_array, region_array, country_array,
			   date_array, description_array, ticket_data)



	# PAGINATION INFORMATION #
	current_page = json_dat["pagination"]["page_number"]
	num_of_pages = json_dat["pagination"]["page_count"]

	# Determine pagination info.
	if current_page < num_of_pages:
		next_page = current_page + 1

	previous_page = current_page - 1

		

	return render(request, "eventful_app/results.html", {
				'api_query': api_query,
				'api_request': api_request, 
				'current_page': current_page,
				'num_of_pages': num_of_pages,
				'next_page' : next_page,
				'previous_page' : previous_page,
				'list': list,
				})
	