import pathlib
import random
import subprocess
from sys import stderr
from typing import List, Union
import os
import argparse
import logging
import config


class player:
    """ Playing the music in a directory (and its subdirectories)
    """

    def __init__(self) -> None:
        self.keepplay = True
        self.P = None
        self.next = []
        self.musics = []
        
    def set_musics(self, paths: List[str]) -> None:
        """ Get musics under paths
        """
        self.musics = []
        for p in paths:
            self.musics.extend(self._get_one_path(p))

    def _get_one_path(self, path: str) -> List[List[str]]:
        """ Fetch musics under path.

        Args:
            path (str): path containing music files

        Returns:
            List[List[str]]: all musics under path, each element in the 
            result represent:
                1. Single file music: [file]
                2. Sonata: [[part_last, ..., part_2, part_1]] 
        """
        res = []
        tmp = {}

        for dirpath, _, filenames in os.walk(path):
            for name in filenames:
                if name.endswith(".flac"):
                    f = os.path.join(dirpath, name)
                    if not player.isSonata(f):
                        res.append([f])
                    else:
                        tmp.setdefault(f[0:-7], []).append(f)
        for m in tmp.values():
            res.append(sorted(m, reverse=True))
        
        return res

    @staticmethod
    def isSonata(f: str) -> bool:
        return len(f) > 7 and f[-7] == ' ' and f[-6].isdigit()


    def start(self):
        """ Blockingly play musics
        """
        if 0 == len(self.musics):
            raise Exception("Did not find any music file under this folder.")

        if self.isplaying():
            return

        self.keepplay = True
        while self.keepplay:
            m = self.NextSong()
            logging.info(m)
            self.P = subprocess.Popen(
                ["ffplay", "-hide_banner", "-autoexit", "-nodisp", m], 
                # stdout=subprocess.DEVNULL,
                # stderr = subprocess.DEVNULL
            )
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
        if self.isplaying():
            self.P.kill()
            self.P.wait()
            self.P = None

    def isplaying(self):
        return self.P != None


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Simple music player.")
    parser.add_argument("paths", action = 'append',
                        help="Path(s) to music folder")
    args = parser.parse_args()
    p = player()
    p.set_musics(args.paths)

    p.start()
