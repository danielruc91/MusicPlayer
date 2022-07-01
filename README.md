# MusicPlayer
Control music palyer through light weight web interface.

## Background
I have a speaker and I use my laptop to play music on it. I use a 3.5mm wired conenction between the laptop and the speaker. Everytime I want to start/stop playing or change song, I have to go to the speaker. But I am very lazy and hence this tiny project. It will run a simple http server which allow you to control the playing behavior, from any device that have access to the network.

If you are like me that:

1. Want to play lossless music so that playing over bluebooth is not an option;
2. Have a stupid speaker that only allow Play-Over-Wifi through Airplay or Spotify Connect, but cannot afford an Apple device nor spotify premium membership;
4. Only need very simple functionality like start/stop and change current song; and 
5. Hate it so much that you have to get out of bed to turn speaker down before sleep...

Try out this tiny toy controller!


## Requirements

The projetc use ffplay to play, so you need to make sure it is discoverable by your shell. (On windows, this means adding ffplay to your Path environment variable).

It uses 'Music' environment variable to look for albums, but you can always supply a specific path to look for files.


## How to use

The server.py will host a simple http server on the machine.
```shell
python server.py
```

Run the above shell and navigate to `127.0.0.1:8000` to see the page.