This is a demo application I built the week of March 16th, 2015 using the Django web development framework. 
It was built as part of the application/interview process for Eventbrite's internship program.

To get it running on localhost, you will want to spin up a Postgres database, and include the necessary
information linking that database in the settings.py file.

Make the first migrations (if thats necessary), and then run them on the database.
As in <code>python manage.py makemigrations</code> and then <code>python manage.py migrate</code>.

At this point you'll want to use a custom admin script to pull the categories off of Eventbrite's
API. To do this run <code>python manage.py mine_categories</code>.

Now <code>python manage.py runserver</code> should have the application running locally.