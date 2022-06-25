import json
import sys

import cherrypy

from lib.constants import DEFAULT_CONFIG_PATH


class Config():

    _config = {}

    @staticmethod
    def load():
        dir = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_CONFIG_PATH

        f = open(dir, "r")
        Config._config = json.load(f)
        f.close()

        cherrypy.config.update(Config._config)

    @staticmethod
    def get(prop):
        return Config._config[prop]
