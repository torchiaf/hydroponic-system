import cherrypy

from lib.api.response import Response

@cherrypy.expose
class WaterRouter(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return Response.msg({'water': '5', 'unit': 'ml'})

    def POST(self):
        return Response.msg({'water': '10', 'unit': 'ml'})