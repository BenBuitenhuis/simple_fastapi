Here's a quick start on deploying a FastAPI app to DigitalOcean's App Platform. FastAPI is a microframework in the same vein as Flask. Because of the similarities, we'll be following the [Flask Quickstart](https://github.com/digitalocean/sample-flask/blob/main/README.md) that DigialOcean provides. You'll first need a [DigitalOcean](https://m.do.co/c/beef14f5483f) account and logged in.

## The `gunicorn.conf.py` & `Procfile` files

The main key to deploying your FastAPI app is setting up the `gunicorn.conf.py` file and a `Procfile`. Your `gunicorn.conf.py` file will look like so:

```python
# -*- coding: utf-8 -*-
"""
Gunicorn with Uvicorn config to launch in Digital Ocean's App Platform.
"""
bind = "0.0.0.0:8080"
workers = 2
# Uvicorn's Gunicorn worker class
worker_class = "uvicorn.workers.UvicornWorker"
```

Here we're following [Gunicorn Configuration](https://docs.gunicorn.org/en/stable/configure.html) basic settings. The settings here are binding the FastAPI app to port `"8080"`, setting 2 workers, you can add more workers or less, and the most important part is `uvicorn`'s `gunicorn` [worker class](https://www.uvicorn.org/deployment/#gunicorn). FastAPI is an async framework so we can't use a WSGI server but must use an ASGI server to serve an asynchronous web framework like FastAPI. Nicely `uvicorn` supplys a worker class to help `gunicorn` serve an async framework like FastAPI. The next file then is the `Procfile` which will look like so:

```
web: gunicorn --worker-tmp-dir /dev/shm --config gunicorn.conf.py src.main:app
```

Once you have those two files you can now just follow the steps below and your FastAPI will deploy!

## Deploy

* Visit https://cloud.digitalocean.com/apps (if you're not logged in, you may see an error message. Visit https://cloud.digitalocean.com/login directly and authenticate, then try again)
* Click "Launch App" or "Create App"
* Choose GitHub and authenticate with your GitHub credentials.
* Under Repository, choose this repository (e.g. <your-org>/sample-flask) and click Next.
* On the next screen you will be prompted for the name of your app, which region you wish to deploy to, which branch you want deployments to spin-off of and whether or not you wish to auto-deploy the app every time an update is made to this branch. Fill this out according to how you want your app to function and click Next.
* Modify the Run Command setting to point to your application. For this example, my project is named mysite. So the modified command would be `gunicorn --worker-tmp-dir /dev/shm --config gunicorn.conf.py src.main:app`
* There is no need to modify the Build Command section
* Confirm your Plan settings and how many containers you want to launch and click Launch Basic/Pro App.
* You should see a "Building..." progress indicator. And you can click "Deployments"→"Details" to see more details of the build.
* It can currently take 5-6 minutes to build this app, so please be patient. Live build logs are coming soon to provide much more feedback during deployments.
* Once the build completes successfully, click the "Live App" link in the header and you should see your running application in a new tab, displaying the home page.

# Conclusion

Hopefully, this quick start got you up and rolling. If you're unfamiliar with [FastAPI](https://fastapi.tiangolo.com/), watch calmcode.io's [video tutorial](https://calmcode.io/fastapi/hello-world.html) on FastAPI. If you're ready to make the switch from Flask to FastAPI, check out Testdriven.io's FastAPI [course](https://testdriven.io/courses/tdd-fastapi/?utm_source=mrcartoonster). If you want me to also write a post on how I built this app, Tweet me at [@mrcartoonster](https://twitter.com/mrcartoonster) or leave a message below that you'd like a tutorial about this example app.
