import cherrypy


@cherrypy.expose
class PositionRouter(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return 'GET position'

    def POST(self):
        return 'POST position'