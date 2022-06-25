import cherrypy


@cherrypy.expose
class CourseRouter(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        return 'Courses GET'

    def POST(self):
        return 'Courses POST'