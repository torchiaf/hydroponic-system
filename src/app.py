import json
import cherrypy

from controllers.main import MainController

f = open('config.json', "r")
config = json.load(f)
f.close()

cherrypy.config.update(config)

if __name__ == '__main__':
    cherrypy.tree.mount(MainController(), '/api/hello', {
        '/': {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
    })
    cherrypy.engine.start()
    cherrypy.engine.block()