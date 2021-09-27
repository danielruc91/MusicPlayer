import pathlib
import random
import subprocess
from typing import List, Union
import os
import argparse
import logging
import config


def isSonata(f: str) -> bool:
    return len(f) > 7 and f[-7] == ' ' and f[-6].isdigit()


class player:
    """ Playing the music in a directory (and its subdirectories)
    """

    def __init__(self, path) -> None:
        self.keepplay = True
        self.P = None
        self.next = []

        self.musics = []
        tmp = {}
        for dirpath, _, filenames in os.walk(path):
            for name in filenames:
                if name.endswidth(".flac"):
                    f = os.path.join(dirpath, name)
                    if not isSonata(f):
                        self.musics.append([f])
                    else:
                        tmp.setdefault(f[0:-7], []).append(f)
        for key in tmp:
            self.musics.append(sorted(tmp[key]))

    def start(self):
        """ Blockingly play musics
        """
        if 0 == len(self.musics):
            raise "Did not find any music file under this folder."

        if self.isplaying():
            return

        self.keepplay = True
        while self.keepplay:
            m = self.NextSong()
            logging.info(m)
            self.P = subprocess.Popen(
                ["ffplay", "-hide_banner", "-autoexit", "-nodisp", m])
            self.P.wait()

    def NextSong(self) -> str:
        """ Pick the next music file (or list of files) to play
        """
        if 0 == len(self.next):
            self.next = random.choice(self.musics).copy()
        return self.next.pop()

    def stop(self):
        self.keepplay = False
        self.next = []
        self.P.kill()
        self.P.wait()
        self.P = None

    def isplaying(self):
        return self.P != None


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simple music player.")
    parser.add_argument("path", metavar="path", nargs='?', default=config.DefaultPath,
                        help="Path to music folder, default to system environment variable")
    arguments = parser.parse_args()
    p = player(arguments.path)

    p.start()
