'''
This web scraper scrapes the NASA, JPL, and Twitter to find current information on Mars.

    NASA: Latest News on Mars Mission
    JPL: Featured Image of Mars
    Twitter: Current Mars Weather
'''

from splinter import Browser
from bs4 import BeautifulSoup

def scrape():
    with Browser("chrome", headless=True) as b:

        # URLS

        nasa_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

        jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

        twitter_url = 'https://twitter.com/marswxreport?lang=en'

        # usgs_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

        urls = [nasa_url, jpl_url, twitter_url]

        for url in urls:
            # For all URLS
            b.visit(url)
            html = b.html
            soup = BeautifulSoup(html, 'html.parser')

            if (url == nasa_url):
                # NASA Scraping
                slide = soup.find('li', class_="slide")
                news_title = slide.find('div', {'class':"content_title"}).string
                news_text = slide.find('div', class_="article_teaser_body").string

            elif (url == jpl_url):
                # JPL Scraping
                slide = soup.find('li', class_="slide").find('div', class_='img')
                img_src = 'https://www.jpl.nasa.gov' + slide.img['src']

            elif (url == twitter_url):
                tweet = soup.find('div', class_="js-tweet-text-container").p.text
                tweet = tweet.split(" ")
                tweet = tweet[0:len(tweet)-1]
                weather = " ".join(tweet)


    # End Browser
    data = {'news_title': news_title,
            'news_text': news_text,
            'feat_img': img_src,
            'weather': weather}
    return data
