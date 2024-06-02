# ds

## What have I already done?

Opened github and logged in to my account <https://github.com/rbennell>

Clicked on the repositories tab. Clicked 'new' and simply copy and pasted the instructions.

## What are we going to do?

* Generate some utility data
* Set up a django project
* Ingest the data
* Set up an api
* Set up a react project
* Visualise it!

Ok, this is a lot, but let's see how we get on.

### Generate some utility data

Let's take a look at generate/generate.py before doing anything. Once we're happy, we'll open a terminal and run the script.
You'll need to change to the /ds directory and run
`$ python3 generate/generate.py`

Lets run it a few more times.

### Set up a django project

We're going to use Django, which is a framework built on python.
I copied the setup from here - <https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/django/>

Docker is a tool that allows us to create containers. You can think of a container as a computer inside your computer. By using docker, we can ensure that every time we build a 'computer within a computer' it will be the same, so we don't have to worry about different things installed on our computer making the setup fiddly and unpredictable. And once we're finished with our container, we can delete it. It's a bit complicated to start, but I've literally just copied the stuff in that script, so we don't even need to worry about what's happening.

For now, if you'd like to see what happened when I ran step 2 in the `Create a Django project` section, you can try it now in the backend_copy directory. just give it a different name to the one I made `;-)`

Maybe try this `$ sudo docker compose run web django-admin startproject composeexample .` and see what happens.

Once we've finished messing around with the new example, we'll take a look at buildings.

Here I have finished following the instructions in the link above.
After that, i've created a new `app` within our project by effectively logging in to the docker container we created and running
`$ python manage.py startapp buildings`.
I then created some new models in models.py, which is a representation of our database tables.
I registered a django admin, added the app in settings.py, then created some migrations and ran them. We can look at everything this has done by logging in to the admin. Let's try it!

go to localhost:8000/admin

Oh, can't log in...
Ok, let's go in our shell and type `$ python manage.py createsuperuser`.
Once we've done this, we can log in, and you can see everything we've created.
Let's play around with the admin.

You can see we can probably create some readings here. But we already created some, so let's import them instead!

### Ingest the data