import cherrypy

from lib.api.response import Response


@cherrypy.expose
class TemperatureRouter(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return Response.msg({'temperature': '20', 'unit': 'C'})