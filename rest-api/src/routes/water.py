import cherrypy


@cherrypy.expose
class WaterRouter(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return 'GET Water'

    def POST(self):
        return 'POST Water'