class Songs:
    """
    represent songs

    Attributes:
        title (str): the title of the song
        artist (Artist): an artist object representing the songs creator
        duration (int): The duration of the song in seconds
    """ 

    def __init__(self,title,artist,duration=0):
        """
        initial method

        """
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """display album using ti's track list
    Attributes:
        album_name (str) : the name of the album.
        year (int) : The year was album was released.
        artist (artist) : who create the song
        if there is no name is define then default artist name will "veronica"
        track (list[song]) : albums list of songs        
    """

    def __init__(self,album_name,year,artist=None):
        self.album_name = album_name
        self.year = year
        if artist is None:
            self.artist = Artist("veronica")
        else:
            self.artist = artist

        self.track = []

    def add_song(self,songs,position=None):
        """add songs to the track
        
        Args:
             songs(song): a list of songs
             position (optional[int]) : if specified,the song will be added to the specific position
                                        otherwise song will be added at the end of the list
        """

        if position is None:
            self.track.append(songs)
        else:
            self.track.insert(position,songs)

class Artist:
    """store the detail of the artist
    Attribute:
        name(str) : name of the artist
        alums(list[int]): list of the only alums those who's not executive list of the artist's pulished albums.
    
    Methods:
        add_albume: use to add new albume to the artist's album of the list
    """

    def __init__(self,name):
        self.name = name
        self.albums = []

    def add_album(self,album):
        """add new albume to the list.
        Args:
            album (Album): albume object to add the list.
                if the albume object is already present, it will not added again(althought this is yet to implemented).                
        """
        self.albums.append(album)
             

def laod_data():
    new_artist = None
    new_albume = None
    artist_list = []

    with open('albums.txt','r') as album:
        for line in album:
            artist , albums , year , song = tuple(line.strip('\n').split('\t'))
            year = int(year)
            print(year,artist,song)


if __name__ == "__main__":
    laod_data( )