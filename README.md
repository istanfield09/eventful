March 25th edit: My deployment to Heroku crashed numerous times due to time out errors. <br />
There is a working deployment on [ianstanfield.com](ianstanfield.com:3000).

This is a demo application I built the week of March 16th, 2015 using the Django web development framework. 
It was built as part of the application/interview process for Eventbrite's internship program.

You will want to create a Python environment and install requirements via pip.<br />
<code>virtualenv eventful</code>
<code>pip install requirements</code>


To get it running on localhost, you will want to spin up a Postgres database, and include the necessary
information linking that database in the settings.py file.

Make the first migrations (if thats necessary), and then run them on the database.
As in <code>python manage.py makemigrations</code> and then <code>python manage.py migrate</code>.

At this point you'll want to use a custom admin script to pull the categories off of Eventbrite's
API. To do this run <code>python manage.py mine_categories</code>.

Now <code>python manage.py runserver</code> should have the application running locally.