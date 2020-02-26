from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import json
import pprint

# GRANT SCRAPER FOR CREATIVE VIC WEBSITE USING BEAUTIFULSOUP 4 TO PARSE TABLE DATA
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

    def print_table_data(self):
        self.table_data = []
        self.table = self.soup.find_all('table')
        for table in self.table:
            for row in table.find_all('tr'):
                tds = row.find_all('td')
                try:
                    program = row.find_all('td')[0].string
                    link = row.find('a').get('href')
                    date = row.find_all('td')[1].string
                    if(date):
                        self.table_data.append({
                            'org': self.org,
                            'program':   program,
                            'link': link,
                            'date': date
                        })
                except:
                    pass
        # Print array
        # pprint.pprint(self.table_data)

    def save_data(self, filename):

        with open(filename, 'w', encoding='utf-8') as outfile:
            json.dump(self.table_data, outfile,  ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # Set Variables
    org = "Creative Victoria"
    grants_url = "https://creative.vic.gov.au/grants-and-support/funding-calendar"
    outfile = "./json/creativevic.json"

    # Instantiate GrantScraper Object with organization as Arguments
    g = GrantScraper(org)
    # Get the page and save as BS4 Object
    g.fetch_page(grants_url)
    g.print_table_data()
    # Save the data as a json object
    g.save_data(outfile)
