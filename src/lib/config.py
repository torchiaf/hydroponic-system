import json

import cherrypy


class Config():

    _config = {}

    @staticmethod
    def load():
        f = open('src/config.json', "r")
        Config._config = json.load(f)
        f.close()

        cherrypy.config.update(Config._config)

    @staticmethod
    def get(prop):
        return Config._config[prop]
