import pathlib
import random
from typing import List, Union
import os
import argparse
import logging


class controller:
    """ Controls playing the music
    """

    def __init__(self, path) -> None:
        self.musics = []
        for dirpath, _, filenames in os.walk(path):
            self.musics.extend([os.path.join(dirpath, name)
                               for name in filenames if name.endswith(".flac")])

    def start(self):
        """ Blockingly play musics
        """
        if 0 == len(self.musics):
            raise "Did not find any music file under this folder."

        while True:
            m = self.NextSong()
            logging.info(m)
            if isinstance(m, str):
                os.system(f'ffplay -nodisp -autoexit "{m}"')
            else:
                for f in m:
                    os.system(f'ffplay -nodisp -autoexit "{f}"')

    def NextSong(self) -> Union[str, List[str]]:
        """ Pick the next music file (or list of files) to play
        """
        # Currently only ramdom running is supported
        # TODO: For sonata, pick all chapters and return in list
        return random.choice(self.musics)


if __name__ == "__main__":
    p = os.path.join(pathlib.Path.home(), "Music")

    parser = argparse.ArgumentParser(description="Simple music player.")
    parser.add_argument("path", metavar="path", nargs='?', default=p,
                        help="Path to music folder, default to system environment variable")
    arguments = parser.parse_args()
    con = controller(arguments.path)

    con.start()
