class Songs:

    def __init__(self,title,artist,duration=0):
        self.title = title
        self.duration = duration
        self.artist = artist

class Album:

    def __init__(self,name,year,artist=None):
        self.name= name
        self.year = year        
        if artist is None:
            self.artist = Artist("veronica")
        else:
            self.artist = artist
        self.track = []

    def add_songs(self,songs,position=None):
        if position is None:
            self.track.append(songs)
        else:
            self.track.insert(position,songs)

class Artist:

    def __init__(self,name):
        self.name = name
        self.alums = []

    def add_albume(self,album):
        self.alums.append(album)

