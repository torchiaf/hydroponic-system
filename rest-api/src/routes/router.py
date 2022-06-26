import cherrypy
from lib.config import Config


class Router():

    _api_version = 'default'

    def __init__(self):
        self._api_version = Config.get('api.version')

    def mount(self, router, path):
        cherrypy.tree.mount(router, f"/{self._api_version}/{path}", {
            '/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        })