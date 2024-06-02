# backend

This is where we'll create our django project. it'll provide an interface between the database and the internet!

I copied the setup from here - <https://github.com/docker/awesome-compose/tree/master/official-documentation-samples/django/>

Docker is a tool that allows us to create containers. You can think of a container as a computer inside your computer. By using docker, we can ensure that every time we build a 'computer within a computer' it will be the same, so we don't have to worry about different things installed on our computer making the setup fiddly and unpredictable. And once we're finished with our container, we can delete it. It's a bit complicated to start, but I've literally just copied the stuff in that script, so we don't even need to worry about what's happening.

For now, if you'd like to see what happened when I ran step 2 in the `Create a Django project` section, you can try it now. just give it a different name to the one I made `;-)`

Maybe try this `$ sudo docker compose run web django-admin startproject composeexample .` and see what happens.
