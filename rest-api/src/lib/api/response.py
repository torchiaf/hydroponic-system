import json

from lib.constants import MACHINE_NUMBER


class Response():

    @staticmethod
    def msg(value, description = 'def'):
        return json.dumps({
            'id': MACHINE_NUMBER,
            'description': description,
            'response': value
            })