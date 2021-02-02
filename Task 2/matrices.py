import nltk
from nltk.metrics.distance import jaro_similarity
import numpy as np

# Defining mediated and datasource attributes
mediated = ["UID", "name", "CCInfo", "PID", "OID", "OID", "UID", "orderNumber", "totalCost", "Adress", "PID", "pizzaName", "nutrition", "price"]
datasource = ["SOPID", "PizzaName", "nurishment", "total", "CID", "PIID", "FirstName", "LastName", "PIID", "CreditCardNumber", "ccv", "expDate", "OID", "CID", "orderCode", "totalAmount", "Adress", "PID", "OID", "PID", "title", "nurishment", "price", "UID", "FirstName", "LastName", "CCNumber", "ccv", "expDate", "OID", "UID", "orderNumber", "Sum", "AID", "OID", "PID", "AID", "User", "street", "city", "zip"]

log = open("Task 2/matrixLog.txt", "w")

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
minzerofive = minimum
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
maxzerofive = maximum
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
avgzerofive = average
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
minzerothree = minimum
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
maxzerothree = maximum
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

# Computing schema matching by tresholding (0.3) for minimum combination
log.write("\n\nSchema matching for average combination strategy by tresholding with value 0.3")

# Initialization of some required variables
treshold = 0.3
avgzerothree = average
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
minzeroseven = minimum
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

# Computing schema matching by tresholding (0.7) for maximumx combination
log.write("\n\nSchema matching for maximum combination strategy by tresholding with value 0.7")

# Initialization of some required variables
treshold = 0.7
maxzeroseven = maximum
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

# Computing schema matching by tresholding (0.7) for minimum combination
log.write("\n\nSchema matching for average combination strategy by tresholding with value 0.7")

# Initialization of some required variables
treshold = 0.7
avgzeroseven = average
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

# Closing the log file - Done~
log.close