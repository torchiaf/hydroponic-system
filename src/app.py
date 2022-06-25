import cherrypy

from lib.config import Config
from routes.course import CourseRouter
from routes.helloworld import HelloWorldRouter
from routes.router import Router


if __name__ == '__main__':

    Config.load()

    router = Router()
    router.mount(HelloWorldRouter(), 'hello-world')
    router.mount(CourseRouter(), 'course')

    cherrypy.engine.start()
    cherrypy.engine.block()