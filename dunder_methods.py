class Album:
    def __init__(self, name, artist, songs, min_duration):
        self.name = name
        self.artist = artist
        self.songs = songs
        self.min_duration = min_duration

    def __str__(self):
        # This acts as a magic method to print out the data
        return (f"--Album Data--\nName:{self.name}\nArtist:{self.artist}\nSongs:{self.songs}\nDuration:{self.min_duration}")

    def __eq__(self, other):
        # 'Magic' class method to prove the equality '==' between a self value, and another value
        return(
            self.name == other.name and
            self.artist == other.artist and
            self.songs == other.songs and
            self.min_duration == other.min_duration
        )

    def __hash__(self):
        # This 'magic' method will hash
        return hash((self.name, self.artist, self.songs, self.min_duration))

    def __add__(self, other):
        return (self.min_duration + other)


newAlbum = Album(name="Utopia", artist="Travis Scott", songs=["HAYENA", "FE!N", "My Eyes", "MELTDOWN"], min_duration=89)

print(str(newAlbum))
print(hash(newAlbum.name))

# Test of hashing and comparison with other values
other_album_name = "DATA"

hashed_other_album_name = hash(other_album_name)
hashed_newAlbum = hash(newAlbum.name)

if hashed_other_album_name == hashed_newAlbum:
    print(True)
else:print(False)

random_min_duration = newAlbum.min_duration + 60
print(random_min_duration)

'''Basically whenever there is an operation that contains any of the
class variables, it's corresponding class magic method 'dunder' should
be created to perform the operation'''

