import nltk
from nltk.metrics.distance import jaro_similarity
import numpy as np

# Defining mediated and datasource attributes
mediated = ["UID", "name", "CCInfo", "PID", "OID", "OID", "UID", "orderNumber", "totalCost", "Adress", "PID", "pizzaName", "nutrition", "price"]
datasource = ["SOPID", "PizzaName", "nurishment", "total", "CID", "PIID", "FirstName", "LastName", "PIID", "CreditCardNumber", "ccv", "expDate", "OID", "CID", "orderCode", "totalAmount", "Adress", "PID", "OID", "PID", "title", "nurishment", "price", "UID", "FirstName", "LastName", "CCNumber", "ccv", "expDate", "OID", "UID", "orderNumber", "Sum", "AID", "OID", "PID", "AID", "User", "street", "city", "zip"]

log = open("Task 2/matrixLog.txt", "w")

# Computing the length datasource attribute with the most characters
maxLength = 0
for i in range (0, len(datasource)):
	if maxLength < len(datasource[i]):
		maxLength = len(datasource[i])
log.write("Maximum length of an datasource attribute: " + str(maxLength))

# Computing Edit-Distance-Matrix
lev=np.zeros((len(mediated), len(datasource)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(datasource)):
		lev[wordI, wordJ] = 1 - nltk.edit_distance(mediated[wordI], datasource[wordJ]) / maxLength

# Logging Edit-Distance-Matrix
log.write("\n\nEdit-Distance-Matrix: \n")
log.write("[")
for wordI in range (0, len(mediated)):
	log.write("(")
	for wordJ in range (0, len(datasource)):
		log.write("" + str(lev[wordI, wordJ]))
		if wordJ != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if wordI != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")


# Computing Jaro-Matrix
jaro=np.zeros((len(mediated), len(datasource)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(datasource)):
		jaro[wordI, wordJ] = jaro_similarity(mediated[wordI], datasource[wordJ])

# Logging Jaro-Matrix
log.write("\n\nJaro-Matrix: \n")
log.write("[")
for wordI in range (0, len(mediated)):
	log.write("(")
	for wordJ in range (0, len(datasource)):
		log.write("" + str(jaro[wordI, wordJ]))
		if wordJ != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if wordI != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")

# Computing Jaccard-Matrix
jaccard=np.zeros((len(mediated), len(datasource)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(datasource)):
		jaccard[wordI, wordJ] = nltk.jaccard_distance(set(mediated[wordI]), set(datasource[wordJ]))

# Logging Jaccard-Matrix
log.write("\n\nJaccard-Matrix: \n")
log.write("[")
for wordI in range (0, len(mediated)):
	log.write("(")
	for wordJ in range (0, len(datasource)):
		log.write("" + str(jaccard[wordI, wordJ]))
		if wordJ != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if wordI != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")

# Computing Minimum-Combined-Matrix
minimum=np.zeros((len(mediated), len(datasource)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(datasource)):
		minimum[wordI, wordJ] = min(lev[wordI, wordJ], jaro[wordI, wordJ], jaccard[wordI, wordJ])

# Logging Minimum-Combined-Matrix
log.write("\n\nMinimum-Combined-Matrix: \n")
log.write("[")
for wordI in range (0, len(mediated)):
	log.write("(")
	for wordJ in range (0, len(datasource)):
		log.write("" + str(minimum[wordI, wordJ]))
		if wordJ != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if wordI != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")

# Computing Maximum-Combined-Matrix
maximum=np.zeros((len(mediated), len(datasource)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(datasource)):
		maximum[wordI, wordJ] = max(lev[wordI, wordJ], jaro[wordI, wordJ], jaccard[wordI, wordJ])

# Logging Maximum-Combined-Matrix
log.write("\n\nMaximum-Combined-Matrix: \n")
log.write("[")
for wordI in range (0, len(mediated)):
	log.write("(")
	for wordJ in range (0, len(datasource)):
		log.write("" + str(maximum[wordI, wordJ]))
		if wordJ != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if wordI != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")

# Computing Average-Combined-Matrix
average=np.zeros((len(mediated), len(datasource)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(datasource)):
		average[wordI, wordJ] = np.mean([lev[wordI, wordJ], jaro[wordI, wordJ], jaccard[wordI, wordJ]])

# Logging Average-Combined-Matrix
log.write("\n\nAverage-Combined-Matrix: \n")
log.write("[")
for wordI in range (0, len(mediated)):
	log.write("(")
	for wordJ in range (0, len(datasource)):
		log.write("" + str(average[wordI, wordJ]))
		if wordJ != (len(datasource) - 1):
			log.write(", ")
	log.write(")")
	if wordI != (len(mediated) - 1):
		log.write("),\n")
	else:
		log.write("]")

log.close