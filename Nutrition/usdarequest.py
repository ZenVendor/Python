import requests
import bs4

sTerms = {
    'qlookup': 'carrots',
    'ds': 'SR'
}
uri = 'https://ndb.nal.usda.gov/ndb/search/list'
sResponse = requests.get(uri, sTerms)

soup = bs4.BeautifulSoup(sResponse.text, 'html.parser')
