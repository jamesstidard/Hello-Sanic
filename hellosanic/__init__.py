from sanic import Sanic
from sanic_rethinkdb import RethinkDB

from hellosanic.api import rest, rpc
from hellosanic.websocket import on_connect

rethinkdb = RethinkDB()


def create_app(config):
    app = Sanic(__name__)
    app.config.from_object(config)
    app.config.db = rethinkdb

    rethinkdb.init_app(app)

    app.blueprint(rpc)
    app.blueprint(rest)
    app.add_websocket_route(on_connect, '/websocket')

    return app
