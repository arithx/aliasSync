import falcon

from api import Sync


def handle_404(req, resp):
    raise falcon.HTTPNotFound(
        description="The requested resource does not exist",
        code=falcon.HTTP_404)

app = falcon.API()
app.add_route(Sync.route, sync())

app.add_sink(handle_404, '')
