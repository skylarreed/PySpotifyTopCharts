import billboard


class Playlist:
    def __init__(self):
        self.name = 'New Playlist'
        self.description = 'Playlist Description'
        self.songs = []

    def set_namedesc(self, name, desc):
        self.name = name
        self.description = desc

    def generate_songs(self, genre, year):
        chart = billboard.ChartData(genre, year)
        for song in chart:
            title = song.title
            artist = song.artist
            new_song = f"{title} {artist}"
            print(new_song)
            self.songs.append(new_song)
