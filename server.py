"""HTTP Server Handeling request to control music playing.
"""


import multiprocessing
import os

import http.server
import time


from player import player
import config
from threading import Thread

with open("index.html", 'r') as f:
    INDEXPAGE = f.read().encode()


class controller:
    def __init__(self) -> None:
        self.player = player(config.DefaultPath)
        self.T = None

    def start(self):
        if self.T == None:
            self.T = Thread(target=self.player.start)
            self.T.start()

    def stop(self):
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
        command = str(self.path)

        print(command)

        if command == r"/Start?":
            CON.start()
        elif command == r"/Stop?":
            CON.stop()
        elif command == r"/Next?":
            CON.next()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(INDEXPAGE)


def test(HandlerClass=MPHandler,
         ServerClass=http.server.HTTPServer):
    http.server.test(HandlerClass, ServerClass)


if __name__ == '__main__':
    test()
