from flask import Flask

app = Flask(__name__)

WELCOME_HOME_TEXT = "This is the guessing song app!"

# Uncomment to enable debugging
# import debugpy; debugpy.listen(5724); debugpy.wait_for_client()

@app.route("/")
def home():
  return "This is the guessing song app!"

if __name__ == '__main__':
  app.run()