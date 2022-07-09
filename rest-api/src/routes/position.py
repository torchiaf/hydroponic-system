import cherrypy

from lib.api.response import Response


@cherrypy.expose
class PositionRouter(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return Response.msg({'position': 'high'})

    def POST(self):
        return Response.msg({'position': 'low'})