import requests

from bs4 import BeautifulSoup



def scrape_competitor_price(url):


    try:


        response = requests.get(
            url,
            timeout=10
        )


        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )


        price = soup.find(
            class_="price"
        )


        if price:


            return float(
                price.text
                .replace("₹","")
                .strip()
            )


        else:

            return None



    except Exception as e:


        print(
            "Scraping Error:",
            e
        )


        return None