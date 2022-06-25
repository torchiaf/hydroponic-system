import cherrypy


@cherrypy.expose
class HelloWorldRouter(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return 'Hello World GET'

    def POST(self):
        return 'Hello World POST'