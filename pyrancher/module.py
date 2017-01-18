# Everything goes here.

import requests as r
import config


# Define a Rancher instance, which contains a list of available projects.

class Instance:

    projects = None

    def __init__(self):
        projects_url = """{}/projects""".format(config.RANCHER_INSTANCE)
        api_key = config.RANCHER_API_KEY
        api_secret = config.RANCHER_SECRET_KEY
        raw_response = r.get(projects_url, auth=(api_key, api_secret)).json()
        self.projects = raw_response['data']

# Define a Rancher project.

class Project:

    project_id = None
    hosts = None
    containers = None
    images = None
    status = None