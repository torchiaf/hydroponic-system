import cherrypy

from controllers.root import RootController
from lib.config import Config


if __name__ == '__main__':

    Config().load()

    cherrypy.tree.mount(RootController(), '/api/hello', {
        '/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    })

    cherrypy.engine.start()
    cherrypy.engine.block()