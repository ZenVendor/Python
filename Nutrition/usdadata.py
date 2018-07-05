import csv
import os
import glob

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

# Check if file exists and has a CSV header. If yes, list existing IDs and their report dates
if os.path.isfile(outFile):
    with open(outFile, 'r') as checkHeader:
        hasHeader = csv.Sniffer().has_header(checkHeader.read(1024))

    if hasHeader:
        with open(outFile, 'r') as checkRecords:
            for i, rec in enumerate(csv.reader(checkRecords, 'nutrition')):
                if i == 0:
                    csvHeader = rec
                    continue
                else:
                    if len(rec) is not 0:
                        csvRows.append(rec)
                        existingItems[rec[0]] = rec[2]

# Process each file
for inFile in glob.glob(inFolder + '*.csv'):

    proxRowNo = 8
    valueColumnNo = 2
    foodItemMeta = {}
    nutritionTable = []

    with open(inFile, 'r') as csvFile:

        wholeCsv = {i: row for i, row in enumerate(csv.reader(csvFile))}

        cat = None

        # Metadata rows
        # USDA Id and Name (Line 3)
        food = wholeCsv[3][0].split(': ')[1]
        foodParts = food.split(',', 1)

        if foodParts[0].isdigit():
            foodItemMeta['USDA Id'] = foodParts[0]
            foodItemMeta['Food Name'] = foodParts[1]
        else:
            if '/' in csvFile.name:
                filename = csvFile.name.split('/')[-1].split('.')[0]
            else:
                filename = csvFile.name.split('\\')[-1].split('.')[0]

            if filename.isdigit():
                foodItemMeta['USDA Id'] = filename

            foodItemMeta['Food Name'] = food

        # Report Date (Line 2)
        reportDate = ''.join(wholeCsv[2]).split(':', 1)[1].strip().split(' ')[:3]
        foodItemMeta['Report Date'] = '{}-{}-{}'.format(reportDate[2], monthNames[reportDate[0]], (reportDate[1]))

        # Check if exists or has to bee updated, else skip
        if foodItemMeta['USDA Id'] in existingItems.keys():
            if foodItemMeta['Report Date'] <= existingItems[foodItemMeta['USDA Id']]:
                break

        existingItems[foodItemMeta['USDA Id']] = foodItemMeta['Report Date']

        # Food Group
        foodItemMeta['Food Group'] = wholeCsv[4][0].split(':', 1)[1]

        # Standard Reference DB (Line 0)
        if 'Standard Reference' in wholeCsv[0][0]:
            foodItemMeta['Source'] = 'SR'
        else:
            foodItemMeta['Source'] = ''

        # Per 100g value column
        for i in reversed(range(7, 9)):
            if wholeCsv[i][0] == 'Proximates':
                proxRowNo = i
                valueColumnNo = i - 1
                break

        # Data rows
        for i, row in wholeCsv.items():
            if i < proxRowNo:
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
