from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/test")
def test():
    return "<h1>This is a test page</h1>"

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/post")
def post():
    return render_template('post.html')

@app.route("/write")
def write():
    return render_template('write.html')

if __name__=="__main__":
    app.run(host="0.0.0.0",port=4106)
