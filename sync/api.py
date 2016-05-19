import json
import os
import sys

import falcon


class Sync(object):
    route = "/"

    def __init__(self):
        self.manager = AliasManager()

    def on_get(self, req, resp):
        resp.data = self.manager.get_aliases()
        resp.content_type = 'application/json'
        reps.status = falcon.HTTP_200

    def on_post(self, req, resp):
        resp.status = self.manager.post_alias(req.data)


class AliasManager(object):
    def __init__(self):
        path = os.path.join(sys.prefix, ".aliasSync", "alias")
        if not os.path.exists(path.rsplit(os.path.sep, 1)[0]):
            os.makedirs(path.rsplit(os.path.sep, 1)[0])
        if not os.path.exists(path):
            open(path, 'a').close()
        self.path = path
        self.aliases = []
        self.populate_aliases()

    def populate_aliases(self):
        with open(self.path, 'r') as f:
            self.aliases = [
                {'name': name, 'ip': ip} for name, ip in line.split('=')
                for line in f.read().split('\n') if line != '']


    def get_aliases(self):
        return json.dumps(self.aliases)

    def post_alias(self, data):
        try:
            data = json.loads(data)
            self.aliases.append({'name': data['name'], 'ip': data['ip']})
            self._write_file()
            return falcon.HTTP_200
        except:
            return falcon.HTTP_400

    def _write_file():
        with open(self.path, 'w') as f:
            for alias in self.aliases:
                f.write('{0}={1}\n'.format(alias['name'], alias['ip']))
