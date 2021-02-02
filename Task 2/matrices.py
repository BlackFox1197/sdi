import nltk
from nltk.metrics.distance import jaro_similarity
import numpy as np

# Defining mediated and datasource attributes
log = open("sdi/Task 2/matrixLog.txt", "w")
mediated = ["UID", "name", "CCInfo", "PID", "OID", "OID", "UID", "orderNumber", "totalCost", "Adress", "PID", "pizzaName", "nutrition", "price"]
datasource = ["SOPID", "PizzaName", "nurishment", "total", "CID", "PIID", "FirstName", "LastName", "PIID", "CreditCardNumber", "ccv", "expDate",
"OID", "CID", "orderCode", "totalAmount", "Adress", "PID", "OID", "PID", "title", "nurishment", "price", "UID", "FirstName", "LastName", "CCNumber",
"ccv", "expDate", "OID", "UID", "orderNumber", "Sum", "AID", "OID", "PID", "AID", "User", "street", "city", "zip"]

# BEGIN - Defining schema matching solution for evaluation
solutionPattern = np.zeros((len(mediated), len(datasource)))

# User - Adding UID-Matches
matches = [4, 23]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[0, match] = 1

# User - Adding name-Matches
matches = [6, 7, 24, 25]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[1, match] = 1

# User - Adding CCInfo-Matches
matches = [10, 11, 12, 26, 27, 28]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[2, match] = 1

# OrderItem - Adding PID-Matches
matches = [17, 35]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[3, match] = 1

# OrderItem - Adding OID-Matches
matches = [18, 34]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[4, match] = 1

# Order - Adding OID-Matches
matches = [12, 29]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[5, match] = 1

# Order - Adding UID-Matches
matches = [13, 30]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[6, match] = 1

# Order - Adding orderNumber-Matches
matches = [14, 31]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[7, match] = 1

# Order - Adding totalCost-Matches
matches = [15, 32]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[8, match] = 1

# Order - Adding Adress-Matches
matches = [16, 38, 39, 40]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[9, match] = 1

# Pizza - Adding PID-Matches
matches = [0, 19]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[10, match] = 1

# Pizza - Adding pizzaName-Matches
matches = [1, 20]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[11, match] = 1

# Pizza - Adding nutrition-Matches
matches = [2, 21]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[12, match] = 1

# Pizza - Adding price-Matches
matches = [3, 22]
for data in range(0, len(datasource)):
	for match in matches:
		solutionPattern[13, match] = 1

# END - Defining schema matching solution for evaluation
# BEGIN - Computing Matrizes

# Computing Edit-Distance-Matrix
lev=np.zeros((len(mediated), len(datasource)))
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		maxLength = max([len(mediated[med]), len(datasource[data])])
		lev[med, data] = 1 - nltk.edit_distance(mediated[med], datasource[data]) / maxLength

# Logging Edit-Distance-Matrix
log.write("\n\nEdit-Distance-Matrix: \n")
log.write("[")
for med in range (0, len(mediated)):
	log.write("(")
	for data in range (0, len(datasource)):
		log.write("" + str(lev[med, data]))
		if data != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if med != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")


# Computing Jaro-Matrix
jaro=np.zeros((len(mediated), len(datasource)))
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		jaro[med, data] = jaro_similarity(mediated[med], datasource[data])

# Logging Jaro-Matrix
log.write("\n\nJaro-Matrix: \n")
log.write("[")
for med in range (0, len(mediated)):
	log.write("(")
	for data in range (0, len(datasource)):
		log.write("" + str(jaro[med, data]))
		if data != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if med != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")

# Computing Jaccard-Matrix
jaccard=np.zeros((len(mediated), len(datasource)))
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		jaccard[med, data] = nltk.jaccard_distance(set(mediated[med]), set(datasource[data]))

# Logging Jaccard-Matrix
log.write("\n\nJaccard-Matrix: \n")
log.write("[")
for med in range (0, len(mediated)):
	log.write("(")
	for data in range (0, len(datasource)):
		log.write("" + str(jaccard[med, data]))
		if data != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if med != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")

# Computing Minimum-Combined-Matrix
minimum=np.zeros((len(mediated), len(datasource)))
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		minimum[med, data] = min(lev[med, data], jaro[med, data], jaccard[med, data])

# Logging Minimum-Combined-Matrix
log.write("\n\nMinimum-Combined-Matrix: \n")
log.write("[")
for med in range (0, len(mediated)):
	log.write("(")
	for data in range (0, len(datasource)):
		log.write("" + str(minimum[med, data]))
		if data != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if med != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")

# Computing Maximum-Combined-Matrix
maximum=np.zeros((len(mediated), len(datasource)))
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		maximum[med, data] = max(lev[med, data], jaro[med, data], jaccard[med, data])

# Logging Maximum-Combined-Matrix
log.write("\n\nMaximum-Combined-Matrix: \n")
log.write("[")
for med in range (0, len(mediated)):
	log.write("(")
	for data in range (0, len(datasource)):
		log.write("" + str(maximum[med, data]))
		if data != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if med != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")

# Computing Average-Combined-Matrix
average=np.zeros((len(mediated), len(datasource)))
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		average[med, data] = np.mean([lev[med, data], jaro[med, data], jaccard[med, data]])

# Logging Average-Combined-Matrix
log.write("\n\nAverage-Combined-Matrix: \n")
log.write("[")
for med in range (0, len(mediated)):
	log.write("(")
	for data in range (0, len(datasource)):
		log.write("" + str(average[med, data]))
		if data != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if med != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")

# Computing schema matching by tresholding (0.5) for minimum combination
log.write("\n\nSchema matching for minimum combination strategy by tresholding with value 0.5")

# Initialization of some required variables
treshold = 0.5
minzerofive = np.copy(minimum)
medKeys = []
dataKeys = []
dataValues = []

# Finding of pairings which accept the treshold constraint
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if minimum[med, data] >= treshold:
			medKeys.append(med)
			dataKeys.append(data)
			dataValues.append(minimum[med, data])
			minzerofive[med, data] = 1
		else:
			minzerofive[med, data] = 0

# Preparation for visualization of the schema matching result
medKeys = np.array(medKeys)
dataKeys = np.array(dataKeys)
dataValues = np.array(dataValues)
currMedKey = -1

# Visualition of the schema matching result
for i in range (0, len(medKeys)):
	if currMedKey != medKeys[i]:
		log.write("\n" + str(mediated[medKeys[i]])+": ")
		currMedKey = medKeys[i]
	else:
		log.write(", ")
	log.write(str(datasource[dataKeys[i]]) + "(" + str(dataValues[i]) + ")")

# Computing schema matching by tresholding (0.5) for maximumx combination
log.write("\n\nSchema matching for maximum combination strategy by tresholding with value 0.5")

# Initialization of some required variables
treshold = 0.5
maxzerofive = np.copy(maximum)
medKeys = []
dataKeys = []
dataValues = []

# Finding of pairings which accept the treshold constraint
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if maximum[med, data] >= treshold:
			medKeys.append(med)
			dataKeys.append(data)
			dataValues.append(maximum[med, data])
			maxzerofive[med, data] = 1
		else:
			maxzerofive[med, data] = 0

# Preparation for visualization of the schema matching result
medKeys = np.array(medKeys)
dataKeys = np.array(dataKeys)
dataValues = np.array(dataValues)
currMedKey = -1

# Visualition of the schema matching result
for i in range (0, len(medKeys)):
	if currMedKey != medKeys[i]:
		log.write("\n" + str(mediated[medKeys[i]])+": ")
		currMedKey = medKeys[i]
	else:
		log.write(", ")
	log.write(str(datasource[dataKeys[i]]) + "(" + str(dataValues[i]) + ")")

# Computing schema matching by tresholding (0.5) for average combination
log.write("\n\nSchema matching for average combination strategy by tresholding with value 0.5")

# Initialization of some required variables
treshold = 0.5
avgzerofive = np.copy(average)
medKeys = []
dataKeys = []
dataValues = []

# Finding of pairings which accept the treshold constraint
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if average[med, data] >= treshold:
			medKeys.append(med)
			dataKeys.append(data)
			dataValues.append(average[med, data])
			avgzerofive[med, data] = 1
		else:
			avgzerofive[med, data] = 0

# Preparation for visualization of the schema matching result
medKeys = np.array(medKeys)
dataKeys = np.array(dataKeys)
dataValues = np.array(dataValues)
currMedKey = -1

# Visualition of the schema matching result
for i in range (0, len(medKeys)):
	if currMedKey != medKeys[i]:
		log.write("\n" + str(mediated[medKeys[i]])+": ")
		currMedKey = medKeys[i]
	else:
		log.write(", ")
	log.write(str(datasource[dataKeys[i]]) + "(" + str(dataValues[i]) + ")")

# Computing schema matching by tresholding (0.3) for minimum combination
log.write("\n\nSchema matching for minimum combination strategy by tresholding with value 0.3")

# Initialization of some required variables
treshold = 0.3
minzerothree = np.copy(minimum)
medKeys = []
dataKeys = []
dataValues = []

# Finding of pairings which accept the treshold constraint
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if minimum[med, data] >= treshold:
			medKeys.append(med)
			dataKeys.append(data)
			dataValues.append(minimum[med, data])
			minzerothree[med, data] = 1
		else:
			minzerothree[med, data] = 0

# Preparation for visualization of the schema matching result
medKeys = np.array(medKeys)
dataKeys = np.array(dataKeys)
dataValues = np.array(dataValues)
currMedKey = -1

# Visualition of the schema matching result
for i in range (0, len(medKeys)):
	if currMedKey != medKeys[i]:
		log.write("\n" + str(mediated[medKeys[i]])+": ")
		currMedKey = medKeys[i]
	else:
		log.write(", ")
	log.write(str(datasource[dataKeys[i]]) + "(" + str(dataValues[i]) + ")")

# Computing schema matching by tresholding (0.3) for maximum combination
log.write("\n\nSchema matching for maximum combination strategy by tresholding with value 0.3")

# Initialization of some required variables
treshold = 0.3
maxzerothree = np.copy(maximum)
medKeys = []
dataKeys = []
dataValues = []

# Finding of pairings which accept the treshold constraint
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if maximum[med, data] >= treshold:
			medKeys.append(med)
			dataKeys.append(data)
			dataValues.append(maximum[med, data])
			maxzerothree[med, data] = 1
		else:
			maxzerothree[med, data] = 0

# Preparation for visualization of the schema matching result
medKeys = np.array(medKeys)
dataKeys = np.array(dataKeys)
dataValues = np.array(dataValues)
currMedKey = -1

# Visualition of the schema matching result
for i in range (0, len(medKeys)):
	if currMedKey != medKeys[i]:
		log.write("\n" + str(mediated[medKeys[i]])+": ")
		currMedKey = medKeys[i]
	else:
		log.write(", ")
	log.write(str(datasource[dataKeys[i]]) + "(" + str(dataValues[i]) + ")")

# Computing schema matching by tresholding (0.3) for average combination
log.write("\n\nSchema matching for average combination strategy by tresholding with value 0.3")

# Initialization of some required variables
treshold = 0.3
avgzerothree = np.copy(average)
medKeys = []
dataKeys = []
dataValues = []

# Finding of pairings which accept the treshold constraint
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if average[med, data] >= treshold:
			medKeys.append(med)
			dataKeys.append(data)
			dataValues.append(average[med, data])
			avgzerothree[med, data] = 1
		else:
			avgzerothree[med, data] = 0

# Preparation for visualization of the schema matching result
medKeys = np.array(medKeys)
dataKeys = np.array(dataKeys)
dataValues = np.array(dataValues)
currMedKey = -1

# Visualition of the schema matching result
for i in range (0, len(medKeys)):
	if currMedKey != medKeys[i]:
		log.write("\n" + str(mediated[medKeys[i]])+": ")
		currMedKey = medKeys[i]
	else:
		log.write(", ")
	log.write(str(datasource[dataKeys[i]]) + "(" + str(dataValues[i]) + ")")

# Computing schema matching by tresholding (0.7) for minimum combination
log.write("\n\nSchema matching for minimum combination strategy by tresholding with value 0.7")

# Initialization of some required variables
treshold = 0.7
minzeroseven = np.copy(minimum)
medKeys = []
dataKeys = []
dataValues = []

# Finding of pairings which accept the treshold constraint
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if minimum[med, data] >= treshold:
			medKeys.append(med)
			dataKeys.append(data)
			dataValues.append(minimum[med, data])
			minzeroseven[med, data] = 1
		else:
			minzeroseven[med, data] = 0

# Preparation for visualization of the schema matching result
medKeys = np.array(medKeys)
dataKeys = np.array(dataKeys)
dataValues = np.array(dataValues)
currMedKey = -1

# Visualition of the schema matching result
for i in range (0, len(medKeys)):
	if currMedKey != medKeys[i]:
		log.write("\n" + str(mediated[medKeys[i]])+": ")
		currMedKey = medKeys[i]
	else:
		log.write(", ")
	log.write(str(datasource[dataKeys[i]]) + "(" + str(dataValues[i]) + ")")

# Computing schema matching by tresholding (0.7) for maximum combination
log.write("\n\nSchema matching for maximum combination strategy by tresholding with value 0.7")

# Initialization of some required variables
treshold = 0.7
maxzeroseven = np.copy(maximum)
medKeys = []
dataKeys = []
dataValues = []

# Finding of pairings which accept the treshold constraint
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if maximum[med, data] >= treshold:
			medKeys.append(med)
			dataKeys.append(data)
			dataValues.append(maximum[med, data])
			maxzeroseven[med, data] = 1
		else:
			maxzeroseven[med, data] = 0

# Preparation for visualization of the schema matching result
medKeys = np.array(medKeys)
dataKeys = np.array(dataKeys)
dataValues = np.array(dataValues)
currMedKey = -1

# Visualition of the schema matching result
for i in range (0, len(medKeys)):
	if currMedKey != medKeys[i]:
		log.write("\n" + str(mediated[medKeys[i]])+": ")
		currMedKey = medKeys[i]
	else:
		log.write(", ")
	log.write(str(datasource[dataKeys[i]]) + "(" + str(dataValues[i]) + ")")

# Computing schema matching by tresholding (0.7) for average combination
log.write("\n\nSchema matching for average combination strategy by tresholding with value 0.7")

# Initialization of some required variables
treshold = 0.7
avgzeroseven = np.copy(average)
medKeys = []
dataKeys = []
dataValues = []

# Finding of pairings which accept the treshold constraint
for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if average[med, data] >= treshold:
			medKeys.append(med)
			dataKeys.append(data)
			dataValues.append(average[med, data])
			avgzeroseven[med, data] = 1
		else:
			avgzeroseven[med, data] = 0

# Preparation for visualization of the schema matching result
medKeys = np.array(medKeys)
dataKeys = np.array(dataKeys)
dataValues = np.array(dataValues)
currMedKey = -1

# Visualition of the schema matching result
for i in range (0, len(medKeys)):
	if currMedKey != medKeys[i]:
		log.write("\n" + str(mediated[medKeys[i]])+": ")
		currMedKey = medKeys[i]
	else:
		log.write(", ")
	log.write(str(datasource[dataKeys[i]]) + "(" + str(dataValues[i]) + ")")

# END - Computing Matrizes
# BEGIN - Computing Matrizes

# Evaluation of schema matching with tresholding (0.5) and minimum combination
log.write("\n\nEvaluation of schema matching with minimum combination strategy and tresholding by 0.5")

truepositive = 0
falsepositive = 0
truenegative = 0
falsenegative = 0

for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if solutionPattern[med, data] == minzerofive[med, data]:
			if solutionPattern[med, data] == 1:
				truepositive = truepositive + 1
			else:
				truenegative = truenegative + 1
		else:
			if solutionPattern[med, data] == 1:
				falsenegative = falsenegative + 1
			else:
				falsepositive = falsepositive + 1

log.write("\nTP: " + str(truepositive))
log.write("\nTN: " + str(truenegative))
log.write("\nFN: " + str(falsenegative))
log.write("\nFP: " + str(falsepositive))

if truepositive != 0 or falsepositive != 0:
	recall = truepositive / (truepositive + falsepositive)
else:
	recall = 0
log.write("\nRecall: " + str(recall))
if truepositive != 0 or falsenegative != 0:
	precision = truepositive / (truepositive + falsenegative)
else:
	precision = 0
log.write("\nPrecision: " + str(precision))

# Evaluation of schema matching with tresholding (0.5) and maximum combination
log.write("\n\nEvaluation of schema matching with maximum combination strategy and tresholding by 0.5")

truepositive = 0
falsepositive = 0
truenegative = 0
falsenegative = 0

for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if solutionPattern[med, data] == maxzerofive[med, data]:
			if solutionPattern[med, data] == 1:
				truepositive = truepositive + 1
			else:
				truenegative = truenegative + 1
		else:
			if solutionPattern[med, data] == 1:
				falsenegative = falsenegative + 1
			else:
				falsepositive = falsepositive + 1

log.write("\nTP: " + str(truepositive))
log.write("\nTN: " + str(truenegative))
log.write("\nFN: " + str(falsenegative))
log.write("\nFP: " + str(falsepositive))

if truepositive != 0 or falsepositive != 0:
	recall = truepositive / (truepositive + falsepositive)
else:
	recall = 0
log.write("\nRecall: " + str(recall))
if truepositive != 0 or falsenegative != 0:
	precision = truepositive / (truepositive + falsenegative)
else:
	precision = 0
log.write("\nPrecision: " + str(precision))

# Evaluation of schema matching with tresholding (0.5) and average combination
log.write("\n\nEvaluation of schema matching with average combination strategy and tresholding by 0.5")

truepositive = 0
falsepositive = 0
truenegative = 0
falsenegative = 0

for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if solutionPattern[med, data] == avgzerofive[med, data]:
			if solutionPattern[med, data] == 1:
				truepositive = truepositive + 1
			else:
				truenegative = truenegative + 1
		else:
			if solutionPattern[med, data] == 1:
				falsenegative = falsenegative + 1
			else:
				falsepositive = falsepositive + 1

log.write("\nTP: " + str(truepositive))
log.write("\nTN: " + str(truenegative))
log.write("\nFN: " + str(falsenegative))
log.write("\nFP: " + str(falsepositive))

if truepositive != 0 or falsepositive != 0:
	recall = truepositive / (truepositive + falsepositive)
else:
	recall = 0
log.write("\nRecall: " + str(recall))
if truepositive != 0 or falsenegative != 0:
	precision = truepositive / (truepositive + falsenegative)
else:
	precision = 0
log.write("\nPrecision: " + str(precision))

# Evaluation of schema matching with tresholding (0.3) and minimum combination
log.write("\n\nEvaluation of schema matching with minimum combination strategy and tresholding by 0.3")

truepositive = 0
falsepositive = 0
truenegative = 0
falsenegative = 0

for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if solutionPattern[med, data] == minzerothree[med, data]:
			if solutionPattern[med, data] == 1:
				truepositive = truepositive + 1
			else:
				truenegative = truenegative + 1
		else:
			if solutionPattern[med, data] == 1:
				falsenegative = falsenegative + 1
			else:
				falsepositive = falsepositive + 1

log.write("\nTP: " + str(truepositive))
log.write("\nTN: " + str(truenegative))
log.write("\nFN: " + str(falsenegative))
log.write("\nFP: " + str(falsepositive))

if truepositive != 0 or falsepositive != 0:
	recall = truepositive / (truepositive + falsepositive)
else:
	recall = 0
log.write("\nRecall: " + str(recall))
if truepositive != 0 or falsenegative != 0:
	precision = truepositive / (truepositive + falsenegative)
else:
	precision = 0
log.write("\nPrecision: " + str(precision))

# Evaluation of schema matching with tresholding (0.3) and maximum combination
log.write("\n\nEvaluation of schema matching with maximum combination strategy and tresholding by 0.3")

truepositive = 0
falsepositive = 0
truenegative = 0
falsenegative = 0

for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if solutionPattern[med, data] == maxzerothree[med, data]:
			if solutionPattern[med, data] == 1:
				truepositive = truepositive + 1
			else:
				truenegative = truenegative + 1
		else:
			if solutionPattern[med, data] == 1:
				falsenegative = falsenegative + 1
			else:
				falsepositive = falsepositive + 1

log.write("\nTP: " + str(truepositive))
log.write("\nTN: " + str(truenegative))
log.write("\nFN: " + str(falsenegative))
log.write("\nFP: " + str(falsepositive))

if truepositive != 0 or falsepositive != 0:
	recall = truepositive / (truepositive + falsepositive)
else:
	recall = 0
log.write("\nRecall: " + str(recall))
if truepositive != 0 or falsenegative != 0:
	precision = truepositive / (truepositive + falsenegative)
else:
	precision = 0
log.write("\nPrecision: " + str(precision))

# Evaluation of schema matching with tresholding (0.3) and average combination
log.write("\n\nEvaluation of schema matching with average combination strategy and tresholding by 0.3")

truepositive = 0
falsepositive = 0
truenegative = 0
falsenegative = 0

for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if solutionPattern[med, data] == avgzerothree[med, data]:
			if solutionPattern[med, data] == 1:
				truepositive = truepositive + 1
			else:
				truenegative = truenegative + 1
		else:
			if solutionPattern[med, data] == 1:
				falsenegative = falsenegative + 1
			else:
				falsepositive = falsepositive + 1

log.write("\nTP: " + str(truepositive))
log.write("\nTN: " + str(truenegative))
log.write("\nFN: " + str(falsenegative))
log.write("\nFP: " + str(falsepositive))

if truepositive != 0 or falsepositive != 0:
	recall = truepositive / (truepositive + falsepositive)
else:
	recall = 0
log.write("\nRecall: " + str(recall))
if truepositive != 0 or falsenegative != 0:
	precision = truepositive / (truepositive + falsenegative)
else:
	precision = 0
log.write("\nPrecision: " + str(precision))

# Evaluation of schema matching with tresholding (0.7) and minimum combination
log.write("\n\nEvaluation of schema matching with minimum combination strategy and tresholding by 0.7")

truepositive = 0
falsepositive = 0
truenegative = 0
falsenegative = 0

for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if solutionPattern[med, data] == minzeroseven[med, data]:
			if solutionPattern[med, data] == 1:
				truepositive = truepositive + 1
			else:
				truenegative = truenegative + 1
		else:
			if solutionPattern[med, data] == 1:
				falsenegative = falsenegative + 1
			else:
				falsepositive = falsepositive + 1

log.write("\nTP: " + str(truepositive))
log.write("\nTN: " + str(truenegative))
log.write("\nFN: " + str(falsenegative))
log.write("\nFP: " + str(falsepositive))

if truepositive != 0 or falsepositive != 0:
	recall = truepositive / (truepositive + falsepositive)
else:
	recall = 0
log.write("\nRecall: " + str(recall))
if truepositive != 0 or falsenegative != 0:
	precision = truepositive / (truepositive + falsenegative)
else:
	precision = 0
log.write("\nPrecision: " + str(precision))

# Evaluation of schema matching with tresholding (0.7) and maximum combination
log.write("\n\nEvaluation of schema matching with maximum combination strategy and tresholding by 0.7")

truepositive = 0
falsepositive = 0
truenegative = 0
falsenegative = 0

for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if solutionPattern[med, data] == maxzeroseven[med, data]:
			if solutionPattern[med, data] == 1:
				truepositive = truepositive + 1
			else:
				truenegative = truenegative + 1
		else:
			if solutionPattern[med, data] == 1:
				falsenegative = falsenegative + 1
			else:
				falsepositive = falsepositive + 1

log.write("\nTP: " + str(truepositive))
log.write("\nTN: " + str(truenegative))
log.write("\nFN: " + str(falsenegative))
log.write("\nFP: " + str(falsepositive))

if truepositive != 0 or falsepositive != 0:
	recall = truepositive / (truepositive + falsepositive)
else:
	recall = 0
log.write("\nRecall: " + str(recall))
if truepositive != 0 or falsenegative != 0:
	precision = truepositive / (truepositive + falsenegative)
else:
	precision = 0
log.write("\nPrecision: " + str(precision))

# Evaluation of schema matching with tresholding (0.7) and average combination
log.write("\n\nEvaluation of schema matching with average combination strategy and tresholding by 0.7")

truepositive = 0
falsepositive = 0
truenegative = 0
falsenegative = 0

for med in range (0, len(mediated)):
	for data in range (0, len(datasource)):
		if solutionPattern[med, data] == avgzeroseven[med, data]:
			if solutionPattern[med, data] == 1:
				truepositive = truepositive + 1
			else:
				truenegative = truenegative + 1
		else:
			if solutionPattern[med, data] == 1:
				falsenegative = falsenegative + 1
			else:
				falsepositive = falsepositive + 1

log.write("\nTP: " + str(truepositive))
log.write("\nTN: " + str(truenegative))
log.write("\nFN: " + str(falsenegative))
log.write("\nFP: " + str(falsepositive))

if truepositive != 0 or falsepositive != 0:
	recall = truepositive / (truepositive + falsepositive)
else:
	recall = 0
log.write("\nRecall: " + str(recall))
if truepositive != 0 or falsenegative != 0:
	precision = truepositive / (truepositive + falsenegative)
else:
	precision = 0
log.write("\nPrecision: " + str(precision))

# END - Computing Matrizes
# Closing the log file - Done~
log.close