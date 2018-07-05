class Record:
    # complete dictionary
    completeDict = {}

    # meta
    usdaId = [None, 'USDA Id']
    usdaName = [None, 'Name']
    usdaRecordDate = [None, 'Record Date']
    usdaFoodGroup = [None, 'Food Group']
    usdaValueColumn = [None, '100g']

    # energy
    energy = [0.0, 'kCal', 'Energy']

    # carbs
    totalCarbs = [0.0, 'g', 'Total Carbs']
    fiber = [0.0, 'g', 'Fiber']
    sugar = [0.0, 'g', 'Sugars']

    # protein
    protein = [0.0, 'g', 'Protein']

    # fats
    totalFat = [0.0, 'g', 'Total Fat']
    satFat = [0.0, 'g', 'Saturated Fat']
    monoFat = [0.0, 'g', 'Monounsaturated Fat']
    polyFat = [0.0, 'g', 'Polyunsaturated Fat']
    transFat = [0.0, 'g', 'Trans Fat']

    # minerals
    ca = [0.0, '', 'Calcium']
    cu = [0.0, '', 'Copper']
    f = [0.0, '', 'Fluoride']
    fe = [0.0, '', 'Iron']
    mg = [0.0, '', 'Magnesium']
    mn = [0.0, '', 'Manganese']
    p = [0.0, '', 'Phosphorus']
    k = [0.0, '', 'Potassium']
    se = [0.0, '', 'Selenium']
    na = [0.0, '', 'Sodium']
    zn = [0.0, '', 'Zinc']

    # vitamins
    vitA = [0.0, '', 'Vitamin A']
    vitB6 = [0.0, '', 'Vitamin B6']
    vitB12 = [0.0, '', 'Vitamin B12']
    vitC = [0.0, '', 'Vitamin C']
    vitD = [0.0, '', 'Vitamin D']
    vitE = [0.0, '', 'Vitamin E']
    vitK = [0.0, '', 'Vitamin K']
    carotA = [0.0, '', 'Carotene Alpha']
    carotB = [0.0, '', 'Carotene Beta']
    betaine = [0.0, '', 'Betaine']
    choline = [0.0, '', 'Choline']
    folate = [0.0, '', 'Folate']
    niacin = [0.0, '', 'Niacin']
    pantoAcid = [0.0, '', 'Pantothenic Acid']
    riboflavin = [0.0, '', 'Riboflavin']
    thiamin = [0.0, '', 'Thiamin']

    proximates = {
        'Energy': energy,
        'Carbohydrate, by difference': totalCarbs,
        'Fiber, total dietary': fiber,
        'Sugars, total': sugar,
        'Protein': protein,
        'Total lipid (fat)': totalFat
    }
    lipids = {
        'Fatty acids, total saturated': satFat,
        'Fatty acids, total monounsaturated': monoFat,
        'Fatty acids, total polyunsaturated': polyFat,
        'Fatty acids, total trans': transFat
    }
    minerals = {
        'Calcium, Ca': ca,
        'Copper, Cu': cu,
        'Fluoride, F': f,
        'Iron, Fe': fe,
        'Magnesium, Mg': mg,
        'Manganese, Mn': mn,
        'Phosphorus, P': p,
        'Potassium, K': k,
        'Selenium, Se': se,
        'Sodium, Na': na,
        'Zinc, Zn': zn
    }
    vitamins = {
        'Vitamin A, IU': vitA,
        'Vitamin B-6': vitB6,
        'Vitamin B-12': vitB12,
        'Vitamin C, total ascorbic acid': vitC,
        'Vitamin D': vitD,
        'Vitamin E (alpha-tocopherol)': vitE,
        'Vitamin K (phylloquinone)': vitK,
        'Carotene, alpha': carotA,
        'Carotene, beta': carotB,
        'Betaine': betaine,
        'Choline, total': choline,
        'Folate, total': folate,
        'Niacin': niacin,
        'Pantothenic acid': pantoAcid,
        'Riboflavin': riboflavin,
        'Thiamin': thiamin
    }

