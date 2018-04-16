from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '<html><a href="/bubi" style="color: red">Go to Bubi</a></html>'

@app.route("/bubi")
def bubi():
    return 'Bubi is the best'

if __name__ == "__main__":
    app.run()