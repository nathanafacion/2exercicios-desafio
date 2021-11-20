import crochet
crochet.setup()

from flask import Flask , render_template, jsonify, request, redirect, url_for
from scrapy import signals
from scrapy.crawler import CrawlerRunner
from scrapy.signalmanager import dispatcher
import time
import os

from scrap.scrap.spiders.aisweb_scraping import AISWebSpider


app = Flask(__name__)

output_data = []
crawl_runner = CrawlerRunner()


@app.route('/')
def index():
	return render_template("index.html") 



@app.route('/', methods=['POST'])
def submit():
    if request.method == 'POST':
        s = request.form['icao']
        global baseURL
        baseURL = 'https://aisweb.decea.mil.br/?i=aerodromos&codigo='+s
        
        return redirect(url_for('search')) 


@app.route("/search")
def search():
    scrape_with_crochet(baseURL=baseURL) 
    time.sleep(10)
    return jsonify(output_data)
  
  
@crochet.run_in_reactor
def scrape_with_crochet(baseURL):
    dispatcher.connect(_crawler_result, signal=signals.item_scraped)
    eventual = crawl_runner.crawl(AISWebSpider, category = baseURL)
    return eventual


def _crawler_result(item, response, spider):
    output_data.append(dict(item))


if __name__== "__main__":
    app.run(debug=True)