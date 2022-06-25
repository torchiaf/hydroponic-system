import cherrypy


@cherrypy.expose
class MainController(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return 'Hello World GET'

    def POST(self, length=8):
        return 'Hello World POST'