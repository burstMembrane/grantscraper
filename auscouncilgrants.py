from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import re
import pprint
# Set Variables
org = "Australia Council"
grants_url = "https://www.australiacouncil.gov.au/funding/"
outfile = "ausdata.json"

# GRANT SCRAPER FOR AUSCOUNCIL WEBSITE USING BEAUTIFULSOUP 4 TO PARSE HTML DATA
# REQUIRES BEAUTIFUL SOUP 4


class GrantScraper:
    def __init__(self, org):
        # Get organisation from global scope
        self.org = org
       
    def fetch_page(self, url):
        # get page
        self.req = Request(url)
        self.raw = urlopen(self.req).read().decode('utf8')
        self.soup = BeautifulSoup(self.raw, 'html.parser')

    def print_html(self):
        print(self.soup.prettify())

    def parse_html(self):
        self.table_data = []
        self.grantslist = self.soup.select('.col-9.content-body li')
        for listitem in self.grantslist:
                
            program = listitem.find('a').text
            #  remove unncessary characters from string using ReGex
            restring = ".*(?=-)"

            program_searched = re.search('[^-]*', program)
            program = program_searched[0]
            link = listitem.find('a', {"class": "btn"}).get('href')
            date = listitem.find('b').parent.text

            if(program and link and date):
                self.table_data.append({
                'organization': self.org, 
                'program':   program,
                'link': link,
                'date': date
                })
            pprint.pprint(self.table_data)

    def save_data(self, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.table_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":

    # Instantiate GrantScraper Object with organization as Arguments
    g = GrantScraper(org)
    # Get the page and save as BS4 Object
    g.fetch_page(grants_url)

    g.parse_html();
    # Save the data as a json object
    g.save_data(outfile)
