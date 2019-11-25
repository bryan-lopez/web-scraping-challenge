from flask import Flask, render_template, redirect, url_for

from pymongo import MongoClient

from scrape_mars import scrape


app = Flask(__name__)

# Start MongoClient
client = MongoClient()
mars = client['mars']
information = mars['information']

# Begin webpage

@app.route("/")
def index():
    info = information.find_one()
    return render_template("index.html", info=info)

@app.route("/scrape")
def scraper():
    data = scrape()
    information.update({}, data, upsert=True)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
