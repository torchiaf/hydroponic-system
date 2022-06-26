import cherrypy


@cherrypy.expose
class TemperatureRouter(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return 'GET temperature'