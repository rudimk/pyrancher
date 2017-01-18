# Everything goes here.

import requests as r
import config
import collections


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
    name = None
    hosts = None
    containers = None
    images = None
    state = None
    health = None
    links = None

    def __init__(self, project_id):
        project_url = """{}/projects/{}""".format(config.RANCHER_INSTANCE, project_id)
        api_key = config.RANCHER_API_KEY
        api_secret = config.RANCHER_SECRET_KEY
        raw_response = r.get(project_url, auth=(api_key, api_secret)).json()
        self.project_id = project_id
        self.name = raw_response['name']
        self.state = raw_response['state']
        self.health = raw_response['healthState']
        self.links = raw_response['links']
    
    def getHosts(self):
        api_key = config.RANCHER_API_KEY
        api_secret = config.RANCHER_SECRET_KEY
        raw_response = r.get(self.links['hosts'], auth=(api_key, api_secret)).json()
        hosts = []
        for host in raw_response['data']:
            payload = collections.OrderedDict()
            payload['uuid'] = host['uuid']
            payload['id'] = host['id']
            payload['name'] = host['name']
            payload['state'] = host['state']
            payload['ip'] = host['agentIpAddress']
            payload['totalMemory'] = host['info']['memoryInfo']['memTotal']
            payload['availableMemory'] = host['info']['memoryInfo']['memAvailable']
            payload['os'] = host['info']['osInfo']['operatingSystem']
            ports = []
            for point in host['publicEndpoints']:
                ports.append(point['port'])
            payload['openPorts'] = ports
            hosts.append(payload)
        self.hosts = hosts





