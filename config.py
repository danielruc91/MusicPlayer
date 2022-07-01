import pathlib
import os

MUSICPATH = os.environ['Music']

ALBUMS = {}
for folder in os.listdir(MUSICPATH):
    p = os.path.join(MUSICPATH, folder)
    if os.path.isdir(p):
        ALBUMS[folder] = p

checkboxes = "".join([ 
    f"""<input type="checkbox" name="albums" value="{album}" checked> {album}<br>"""
    for album in ALBUMS.keys()
])

HTML = f"""
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Let's Play</title>
</head>

<body>
    <form action="/Start">
        {checkboxes}
        <input type="submit" value="Start" />
    </form>
    <form action="Stop">
        <input type="submit" value="Stop" />
    </form>
    <form action="Next">
        <input type="submit" value="Next" />
    </form>
</body>

</html>
""".encode('UTF-8')