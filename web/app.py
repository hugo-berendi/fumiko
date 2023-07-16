from flask import Flask
    
app = Flask(__name__)

    
@app.route("/test")
def test():
	site = open("/home/kamachi/Development/fumiko/web/sites/test.html")
	return site.read()


@app.route("/")
def index():
	site = open("/home/kamachi/Development/fumiko/web/sites/index.html")
	return site.read()


app.run(host='0.0.0.0', port=5000)
