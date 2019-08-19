class Song:
  """
  Class to represent a song

  Attributes:
    title (str): the title of the song.
    artist (str): name of the song creator
    duration (int): the duration of the song in seconds.
  """

  def __init__(self, title, artist, duration = 0):
    self.title = title
    self.artist = artist
    self.duration = duration

  def get_title(self):
    return self.title
  
  name = property(get_title)

# print(Song.__doc__)

class Album:
  """
  Class to represent an album

  Attributes:
    name (str)
    year (int)
    artist (str)
    tracks (List[Song])

  Methods:
    add_song: add new song to album's track list
  """

  def __init__(self, name, year, artist=None):
    self.name = name
    self.year = year

    if artist is None:
      self.artist = "Varios Artists"
    else:
      self.artist = artist

    self.tracks =[]
  
  def add_song(self, song, position=None):
    song_found = find_object(song, self.tracks)
    if song_found is None:
      song_found = Song(song, self.artist)
      if position is None:
        self.tracks.append(song_found)
      else:
        self.tracks.insert(position, song_found)

class Artist:
  """
  Class to represent an artist

  Attributes:
    name (str)
    albums (List[Album])

  Methods:
    add_album
  """

  def __init__(self, name):
    self.name = name
    self.albums = []

  def add_album(self, album):
    self.albums.append(album)

  def add_song(self, name, year, title):
    album_found = find_object(name, self.albums)
    if album_found is None:
      print(name + " not found")
      album_found = Album(name, year, self.name)
      self.add_album(album_found)
    else:
      print("Found album " + name)

    album_found.add_song(title);

def find_object(field, object_list):
  for item in object_list:
    if item.name == field:
      return item

  return None

def load_data():
  new_artist = None
  new_album = None
  artist_list = []

  with open("albums.txt", "r") as albums:
    for line in albums:
      artist_field, album_field, year_field, song_field = tuple(line.strip("\n").split("\t"))
      year_filed = int(year_field)
      print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

      new_artist = find_object(artist_field, artist_list)
      if new_artist is None:
        new_artist = Artist(artist_field)
        artist_list.append(new_artist)
        
      new_artist.add_song(album_field, year_field, song_field)

  return artist_list

def create_checkfile(artist_list):

  with open("checkfile.txt", "w") as checkfile:
    for new_artist in artist_list:
      for new_album in new_artist.albums:
        for new_song in new_album.tracks:
          print("{0.name}\t{1.name}\t{1.year}\t{2.title}\t".format(new_artist, new_album, new_song), file=checkfile)

if __name__ == "__main__":
  artists = load_data()
  print("There are {} artist".format(len(artists)))

  create_checkfile(artists)