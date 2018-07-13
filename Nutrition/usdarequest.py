import requests
import bs4

csvFolder = 'csvdata/'
sTerms = {'ds': 'SR'}

sTerms['qlookup'] = input('Enter search term: ')
uri = 'https://ndb.nal.usda.gov/ndb/search/list'
sResponse = requests.get(uri, sTerms)

sResult = []
soup = bs4.BeautifulSoup(sResponse.text, 'html.parser')
for item in soup.find_all('a', attrs={'title': 'Click to view reports for this food'}):
    sResult.append(item.text.strip().split(' ', 1))

for i in range(len(sResult)):
    print('{}: {}'.format(i, sResult[i][1]))

rNum = int(input('Entry number: '))
reportUrl = 'https://ndb.nal.usda.gov/ndb/foods/show/{}?format=Full&reportfmt=csv&Qv=1'.format(sResult[rNum][0])

print(reportUrl)
rResponse = requests.get(reportUrl)
filename = csvFolder + sResult[rNum][0] + '.csv'
with open(filename, 'wb') as csvFile:
    for chunk in rResponse.iter_content(100000):
        csvFile.write(chunk)


print('Complete: {}'.format(filename))


