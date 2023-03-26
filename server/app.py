from flask import Flask
from protos.song_pb2 import Song, Artist, OTHERS, FEMALE, MALE

app = Flask(__name__)

WELCOME_HOME_TEXT = "This is the guessing song app!"

ARTIST1 = Artist(name="Tri", gender=FEMALE)
ARTIST2 = Artist(name="Tuong", gender=OTHERS)
SONG1 = Song(name="Hello", artists=[ARTIST1, ARTIST2])
SONG2 = Song(name="World", artists=[ARTIST2])

# Uncomment to enable debugging
print("Please start debugging client from VSCODE")
import debugpy; debugpy.listen(5724); debugpy.wait_for_client()

@app.route("/")
def home():
  return "Hello"

@app.route('/songs/<song_name>')
def get_song(song_name):
    matched_songs = list(filter(lambda song: song.name == song_name, [SONG1, SONG2]))
    if not matched_songs:
      return "Song not found"

    return str(matched_songs[0])


if __name__ == '__main__':
  app.run()