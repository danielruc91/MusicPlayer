"""HTTP Server Handeling request to control music playing.
"""


import multiprocessing
import os

import http.server
import urllib.parse as parse
import time

from player import player
import config
from threading import Thread


with open('favicon.ico', 'rb') as f:
    ICO = f.read()


class controller:
    def __init__(self) -> None:
        self.player = player()
        self.T = None

    def set_musics(self, albums):
        paths = [ config.ALBUMS[album] for album in albums ]
        self.player.set_musics(paths)

    def start(self, albums = None):
        if self.T == None:
            # Currently not playing
            if albums:
                # need to set new musics
                self.set_musics(albums)
            
            self.T = Thread(target=self.player.start)
            self.T.start()

    def stop(self):
        print(self.player.isplaying())
        if self.player.isplaying():
            self.player.stop()
            self.T.join()
            self.T = None

    def next(self):
        self.stop()
        self.start()


CON = controller()


class MPHandler(http.server.BaseHTTPRequestHandler):
    """Simple HTTP request handler with GET/HEAD/POST commands.

    Get: Return a simple index page
    Post:
        Start: start playing
        Stop: stops playing
        Next: jump to next song

    """

    def do_GET(self):
        """Serve a GET request."""
        url = parse.urlparse(self.path)

        if url.path == r"/Start":
            query = parse.parse_qs(url.query)
            CON.start(query["albums"])
        elif url.path == r"/Stop":
            CON.stop()
        elif url.path == r"/Next":
            CON.next()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if url.path == r'/favicon.ico':
            self.wfile.write(ICO)
        else:
            self.wfile.write(config.HTML)


def test(HandlerClass=MPHandler,
         ServerClass=http.server.HTTPServer):
    http.server.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()
