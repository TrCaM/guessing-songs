from flask import Flask
from protos.song_pb2 import Song

app = Flask(__name__)

WELCOME_HOME_TEXT = "This is the guessing song app!"

# Uncomment to enable debugging
# import debugpy; debugpy.listen(5724); debugpy.wait_for_client()
# print("Please start debugging client from VSCODE")

@app.route("/")
def home():
  song = Song()
  song.name = "Hello"
  return song.name

if __name__ == '__main__':
  app.run()