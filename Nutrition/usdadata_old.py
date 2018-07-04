import csv, os, glob

# script processes files downloaded from USDA Food Composition Databases https://ndb.nal.usda.gov/ndb
# Standard reference database (generic foods), full report, csv
# nutrition data files stored in inFolder are processed into rows in a single csv outFile
# items that already exist in the output file are not processed again

inFolder = 'csvdata/'
outFile = 'nutritionTable.csv'

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
itemIds = []

csv.register_dialect('nutrition', delimiter=';', quoting=csv.QUOTE_ALL)

if os.path.isfile(outFile):
    with open(outFile, 'r') as check:
        hasHeader = csv.Sniffer().has_header(check.read(128))

        lines = csv.reader(check, 'nutrition')
        for line in lines:
            itemIds.append(line[0])

for inFile in glob.glob(inFolder + '*.csv'):

    foodId = None
    foodName = None
    nutritionTable = []

    with open(inFile, 'r') as csvFile:

        filename = csvFile.name.split('\\')[-1].split('.')[0]
        if filename.isdigit():
            foodId = filename

        wholeCsv = enumerate(csv.reader(csvFile))
        cat = None
        for i, row in wholeCsv:
            if i == 3:
                food = row[0].split(': ')[1]
                foodParts = food.split(',', 1)

                if not foodId and foodParts[0].isdigit():
                    foodId = foodParts[0]
                    foodName = foodParts[1]
                else:
                    foodName = food

                if foodId in itemIds:
                    break

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

        else:
            csvHeader = ['USDA Id', 'Item']
            csvRow = [foodId, foodName]

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