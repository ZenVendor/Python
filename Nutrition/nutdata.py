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

filename = None

reportMeta = {
    'USDA Id': '',
    'Report Date': '',
    'Food Group': '',
    '100g Column': 0,
    'startRowNo': 0,
    'endRowNo': 0
}

with open('csvdata/12142.csv', 'r') as reportFile:
    reportMeta['USDA Id'] = reportFile.name.split('\\')[-1].split('/')[-1].split('.')[0]
    wholeReport = {i: row for i, row in enumerate(csv.reader(reportFile))}

dateParts = wholeReport[2][0].split(':', 1)[1].strip().split(' ')[:3]
reportMeta['Report Date'] = [dateParts[2], monthNames[dateParts[0]], dateParts[1]]
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

print(reportMeta)