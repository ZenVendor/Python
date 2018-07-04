import csv, os, glob

# script processes files downloaded from USDA Food Composition Databases https://ndb.nal.usda.gov/ndb
# Standard reference database (generic foods), full report, csv
# nutrition data files stored in inFolder are processed into rows in a single csv outFile
# items that already exist in the output file are not processed again

inFolder = 'csvdata/'
outFile = 'nutritionTable.csv'

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

proximates = ['Energy', 'Carbohydrate, by difference', 'Fiber, total dietary', 'Sugars, total', 'Protein', 'Total lipid (fat)']
lipids = ['Fatty acids, total saturated', 'Fatty acids, total monounsaturated', 'Fatty acids, total polyunsaturated', 'Fatty acids, total trans']
minerals = ['Calcium, Ca', 'Copper, Cu', 'Fluoride, F', 'Iron, Fe', 'Magnesium, Mg', 'Manganese, Mn', 'Phosphorus, P', 'Potassium, K', 'Selenium, Se', 'Sodium, Na', 'Zinc, Zn']
vitamins = ['Vitamin A, IU', 'Vitamin B-6', 'Vitamin B-12', 'Vitamin C, total ascorbic acid', 'Vitamin D', 'Vitamin E (alpha-tocopherol)', 'Vitamin K (phylloquinone)', 'Carotene, alpha', 'Carotene, beta', 'Betaine', 'Choline, total', 'Folate, total', 'Niacin', 'Pantothenic acid', 'Riboflavin', 'Thiamin']

categories = {
    'Proximates': proximates,
    'Lipids': lipids,
    'Minerals': minerals,
    'Vitamins': vitamins
}

csvHeader = None
csvRows = []

hasHeader = False
existingItems = {}

csv.register_dialect('nutrition', delimiter=';', quoting=csv.QUOTE_ALL)

if os.path.isfile(outFile):
    with open(outFile, 'r') as check:
        hasHeader = csv.Sniffer().has_header(check.read(128))

        lines = csv.reader(check, 'nutrition')
        for line in lines:
            existingItems[line[0]] = line[2]

for inFile in glob.glob(inFolder + '*.csv'):

    foodItemMeta = {}
    nutritionTable = []

    with open(inFile, 'r') as csvFile:

        wholeCsv = enumerate(csv.reader(csvFile))
        cat = None

        meta = [row for i, row in wholeCsv if i in [0, 2, 3]]

        food = meta[2][0].split(': ')[1]
        foodParts = food.split(',', 1)

        filename = csvFile.name.split('\\')[-1].split('.')[0]

        print(filename)

        if filename.isdigit():
            foodItemMeta['USDA Id'] = filename

        if foodParts[0].isdigit():
            foodItemMeta['USDA Id'] = foodParts[0]
            foodItemMeta['Food Name'] = foodParts[1]
        else:
            foodItemMeta['Food Name'] = food

        reportDate = ''.join(meta[1]).split(':', 1)[1].strip().split(' ')[:3]
        foodItemMeta['Report Date'] = '{}-{}-{}'.format(reportDate[2], monthNames[reportDate[0]], (reportDate[1]))

        if foodItemMeta['USDA Id'] in existingItems.keys() and foodItemMeta['Report Date'] == existingItems[foodItemMeta['USDA Id']]:
            break

        print('still going')

        if 'Standard Reference' in meta[0][0]:
            foodItemMeta['Source'] = 'SR'
        else:
            foodItemMeta['Source'] = ''

        for i, row in wholeCsv:
            if i < 9:
                continue

            elif len(row) == 1:
                cat = row[0]
                continue

            elif cat not in categories:
                continue

            else:
                if cat == 'Proximates':
                    if row[1] == 'kJ':
                        continue
                nutritionTable.append([cat, row[0], row[1], str(row[2]).replace('.', ',')])

        csvHeader = []
        csvRow = []

        for head, val in foodItemMeta.items():
                csvHeader.append(head)
                csvRow.append(val)

        for k, v in categories.items():
            for item in v:
                for nut in nutritionTable:
                    if nut[0] == k and nut[1] == item:
                        csvHeader.append('{} [{}]'.format(nut[1], nut[2]))
                        csvRow.append('{}'.format(nut[3]))
                        break
                else:
                    csvHeader.append(item)
                    csvRow.append('---')

        csvRows.append(csvRow)

if len(csvRows) > 0:

    with open(outFile, 'a', newline='') as output:
        out = csv.writer(output, 'nutrition')
        if not hasHeader:
            out.writerow(csvHeader)
        out.writerows(csvRows)
