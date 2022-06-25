import json

import cherrypy


class Config():

    def load(self):
        f = open('src/config.json', "r")
        config = json.load(f)
        f.close()

        cherrypy.config.update(config)