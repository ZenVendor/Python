import csv

monthNames = {
    'January': '01',
    'February': '02',
    'March': '03',
    'April': '04',
    'May': '05',
    'June': '06',
    'July': '07',
    'August': '08',
    'September': '09',
    'October': '10',
    'November': '11',
    'December': '12',
}

reportMeta = {
    'USDA Id': '',
    'Food Name': '',
    'Food Group': '',
    'Report Date': '',
    '100g Column': 0,
    'startRowNo': 0,
    'endRowNo': 0
}

with open('csvdata/12142.csv', 'r') as reportFile:
    reportMeta['USDA Id'] = reportFile.name.split('\\')[-1].split('/')[-1].split('.')[0]
    wholeReport = {i: row for i, row in enumerate(csv.reader(reportFile))}

dateParts = wholeReport[2][0].split(':', 1)[1].strip().split(' ')[:3]
reportMeta['Report Date'] = [dateParts[2], monthNames[dateParts[0]], dateParts[1]]

reportMeta['Food Name'] = wholeReport[3][0].split(':')[1].split(', ')
reportMeta['Food Group'] = wholeReport[4][0].split(':')[1].strip()


for i in reversed(range(7, 10)):
    if wholeReport[i][0] == 'Proximates':
        reportMeta['startRowNo'] = i
        reportMeta['100g Column'] = wholeReport[i-1].index('1Value per 100 g')
        break

for i in reversed(range(reportMeta['startRowNo'], len(wholeReport))):
    if wholeReport[i][0] == 'Sources of Data':
        reportMeta['endRowNo'] = i
        break

foodItem = {}
category = None


for i in range(reportMeta['startRowNo'], reportMeta['endRowNo']):
    if len(wholeReport[i]) == 0:
        continue
    elif len(wholeReport[i]) == 1:
        category = wholeReport[i][0]
        foodItem[category] = {}
    else:
        foodItem[category][wholeReport[i][0]] = [wholeReport[i][1], wholeReport[i][reportMeta['100g Column']]]


for meta in reportMeta.items():
    print(meta)

print()

for cat, nutrient in foodItem.items():
    for nut, val in nutrient.items():
        print('{} - {} [{}]: {}'.format(cat, nut, val[0], val[1]))

