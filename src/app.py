import cherrypy

from lib.config import Config
from routes.position import PositionRouter
from routes.router import Router
from routes.temperature import TemperatureRouter
from routes.water import WaterRouter


if __name__ == '__main__':

    Config.load()

    router = Router()
    router.mount(WaterRouter(), 'water')
    router.mount(PositionRouter(), 'position')
    router.mount(TemperatureRouter(), 'temperature')

    cherrypy.engine.start()
    cherrypy.engine.block()