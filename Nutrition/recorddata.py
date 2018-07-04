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


foodItemMeta = {}

with open('csvdata/11529.csv', 'r') as csvFile:

    wholeCsv = enumerate(csv.reader(csvFile))

    meta = [row for i, row in wholeCsv if i in [0, 2, 3, 8]]

    food = meta[2][0].split(': ')[1]
    foodParts = food.split(',', 1)

    filename = csvFile.name.split('/')[-1].split('.')[0]
    if filename.isdigit():
        foodItemMeta['USDA Id'] = filename

    if foodParts[0].isdigit():
        foodItemMeta['USDA Id'] = foodParts[0]
        foodItemMeta['Food Name'] = foodParts[1]
    else:
        foodItemMeta['Food Name'] = food

    if 'Standard Reference' in meta[0][0]:
        foodItemMeta['Source'] = 'SR'
    else:
        foodItemMeta['Source'] = ''

    reportDate = meta[1][0].split(':', 1)[1].strip().split(' ')[:3]
    foodItemMeta['Report Date'] = '{}-{}-{}'.format(reportDate[2], monthNames[reportDate[0]], (reportDate[1]))

    foodItemMeta['Value Column'] = meta[3].index('1Value per 100 g')

    print(foodItemMeta)
