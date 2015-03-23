from django.core.management.base import BaseCommand

from eventful_app.models import Category

import json
import urllib2

# This custom administration command is used to seed the database with the
# event categories that are available on Eventbrite's API.

# To use this command run 'python manage.py mine_categories'.
# I would probably only do this once as the script
# doesn't detect if category objects already exist or not.

class Command(BaseCommand):

	 def handle(self, *args, **options):
		raw = urllib2.urlopen('https://www.eventbriteapi.com/v3/categories/?token=6W6MK2IRTGDVSXQM3MNY')
		rawU = json.load(raw)

		outputs = rawU['categories']

		for o in outputs:

			outgoing_id_num = o['id']
			outgoing_resource_uri = o['resource_uri']
			outgoing_name = o['name']
			outgoing_name_localized = o['name_localized'] 
			outgoing_short_name = o['short_name']
			outgoing_short_name_localized = o['short_name_localized']

			record = Category(category_id = outgoing_id_num, resource_uri = outgoing_resource_uri, name = outgoing_name, 
							  name_localized = outgoing_name_localized, short_name = outgoing_short_name_localized,
							  short_name_localized = outgoing_short_name_localized)
			record.save()





