class Record:
    # complete dictionary
    completeDict = {}

    # meta
    usdaId = ['', 'USDA Id']
    usdaName = ['', 'Name']
    usdaRecordDate = ['', 'Record Date']
    usdaFoodGroup = ['', 'Food Group']
    usdaValueColumn = ['', '100g']

    # energy
    energy = {'Value': 0.0, 'Unit': 'kCal', 'Name': 'Energy'}

    # carbs
    totalCarbs = {'Value': 0.0, 'Unit': '', 'Name': 'Total Carbs'}
    fiber = {'Value': 0.0, 'Unit': '', 'Name': 'Fiber'}
    sugar = {'Value': 0.0, 'Unit': '', 'Name': 'Sugars'}

    # protein
    protein = {'Value': 0.0, 'Unit': '', 'Name': 'Protein'}

    # fats
    totalFat = {'Value': 0.0, 'Unit': '', 'Name': 'Total Fat'}
    satFat = {'Value': 0.0, 'Unit': '', 'Name': 'Saturated Fat'}
    monoFat = {'Value': 0.0, 'Unit': '', 'Name': 'Monounsaturated Fat'}
    polyFat = {'Value': 0.0, 'Unit': '', 'Name': 'Polyunsaturated Fat'}
    transFat = {'Value': 0.0, 'Unit': '', 'Name': 'Trans Fat'}

    # minerals
    ca = {'Value': 0.0, 'Unit': '', 'Name': 'Calcium'}
    cu = {'Value': 0.0, 'Unit': '', 'Name': 'Copper'}
    f = {'Value': 0.0, 'Unit': '', 'Name': 'Fluoride'}
    fe = {'Value': 0.0, 'Unit': '', 'Name': 'Iron'}
    mg = {'Value': 0.0, 'Unit': '', 'Name': 'Magnesium'}
    mn ={'Value': 0.0, 'Unit': '', 'Name': 'Manganese'}
    p = {'Value': 0.0, 'Unit': '', 'Name': 'Phosphorus'}
    k = {'Value': 0.0, 'Unit': '', 'Name': 'Potassium'}
    se = {'Value': 0.0, 'Unit': '', 'Name': 'Selenium'}
    na = {'Value': 0.0, 'Unit': '', 'Name': 'Sodium'}
    zn = {'Value': 0.0, 'Unit': '', 'Name': 'Zinc'}

    # vitamins
    vitA = {'Value': 0.0, 'Unit': '', 'Name': 'Vitamin A'}
    vitB6 = {'Value': 0.0, 'Unit': '', 'Name': 'Vitamin B6'}
    vitB12 = {'Value': 0.0, 'Unit': '', 'Name': 'Vitamin B12'}
    vitC = {'Value': 0.0, 'Unit': '', 'Name': 'Vitamin C'}
    vitD = {'Value': 0.0, 'Unit': '', 'Name': 'Vitamin D'}
    vitE = {'Value': 0.0, 'Unit': '', 'Name': 'Vitamin E'}
    vitK = {'Value': 0.0, 'Unit': '', 'Name': 'Vitamin K'}
    carotA = {'Value': 0.0, 'Unit': '', 'Name': 'Carotene Alpha'}
    carotB = {'Value': 0.0, 'Unit': '', 'Name': 'Carotene Beta'}
    betaine = {'Value': 0.0, 'Unit': '', 'Name': 'Betaine'}
    choline = {'Value': 0.0, 'Unit': '', 'Name': 'Choline'}
    folate = {'Value': 0.0, 'Unit': '', 'Name': 'Folate'}
    niacin = {'Value': 0.0, 'Unit': '', 'Name': 'Niacin'}
    pantoAcid = {'Value': 0.0, 'Unit': '', 'Name': 'Pantothenic Acid'}
    riboflavin = {'Value': 0.0, 'Unit': '', 'Name': 'Riboflavin'}
    thiamin = {'Value': 0.0, 'Unit': '', 'Name': 'Thiamin'}

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
    categories = {
        'Proximates': proximates,
        'Lipids': lipids,
        'Minerals': minerals,
        'Vitamins': vitamins
    }