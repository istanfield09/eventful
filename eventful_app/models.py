from django.db import models

# Some (most) of the parsed attributes for this model are never used in this 
# application, forgive me!

class Category(models.Model):
	category_id = models.PositiveSmallIntegerField()
	resource_uri = models.URLField()
	name = models.TextField()
	name_localized = models.TextField()
	short_name = models.TextField()
	short_name_localized = models.TextField()



