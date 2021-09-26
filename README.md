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
The project is written in python, so the machine shall be able to run Python. (Yeah, Raspberry Pi is a good option! Consider adding a professional DAC hat for it!)

The projetc use ffplay to play, so you need to make sure it is discoverable by your shell. (On windows, this means adding ffplay to your Path environment variable).

It uses 'Music' folder under your home directory as the folder of your music collection. It will loop into the folder recursively to get all flac files.
1. On windows, this means 'C:/Users/USERNAME/Music'
2. On Linux, this means '~/Music'

But you can always supply a specific path to look for files.


## How to use
Currently, I have finished the controller part. You can run the playing function by simply in your shell:
```shell
python controller.py <path>
```

I am working hard on the server part, but please be notified that I am lazy...

Good luck!