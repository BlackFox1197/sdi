import nltk 
from nltk.metrics.distance import jaro_similarity
import numpy as np
import time

mediated = ["UID", "name", "CCInfo", "PID", "OID", "OID", "UID", "orderNumber", "totalCost", "Adress", "PID", "pizzaName", "nutrition", "price"]

s1s2 = ["SOPID", "PizzaName", "nurishment", "total", "CID", "PIID", "FirstName", "LastName", "PIID", "CreditCardNumber", "ccv", "expDate", "OID", "CID", "orderCode", "totalAmount", "Adress", "PID", "OID", "PID", "title", "nurishment", "price", "UID", "FirstName", "LastName", "CCNumber", "ccv", "expDate", "OID", "UID", "orderNumber", "Sum", "AID", "OID", "PID", "AID", "User", "street", "city", "zip"]

# Computing Edit-Distance-Matrix
lev=np.zeros((len(mediated), len(s1s2)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(s1s2)):
		lev[wordI, wordJ] = nltk.edit_distance(mediated[wordI], s1s2[wordJ])
print(lev)
time.sleep(5)

# Computing Jaro-Matrix
jaro=np.zeros((len(mediated), len(s1s2)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(s1s2)):
		jaro[wordI, wordJ] = jaro_similarity(mediated[wordI], s1s2[wordJ])
print(jaro)
time.sleep(5)

# Computing Jaccard-Matrix
jaccard=np.zeros((len(mediated), len(s1s2)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(s1s2)):
		jaccard[wordI, wordJ] = nltk.jaccard_distance(set(mediated[wordI]), set(s1s2[wordJ]))
print(jaccard)
time.sleep(5)

# Computing Minimum-Combined-Matrix
minimum=np.zeros((len(mediated), len(s1s2)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(s1s2)):
		minimum[wordI, wordJ] = min(lev[wordI, wordJ], jaro[wordI, wordJ], jaccard[wordI, wordJ])
print(minimum)
time.sleep(5)

# Computing Maximum-Combined-Matrix
maximum=np.zeros((len(mediated), len(s1s2)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(s1s2)):
		maximum[wordI, wordJ] = max(lev[wordI, wordJ], jaro[wordI, wordJ], jaccard[wordI, wordJ])
print(maximum)
time.sleep(5)

# Computing Average-Combined-Matrix
average=np.zeros((len(mediated), len(s1s2)))
for wordI in range (0, len(mediated)):
	for wordJ in range (0, len(s1s2)):
		average[wordI, wordJ] = np.mean([lev[wordI, wordJ], jaro[wordI, wordJ], jaccard[wordI, wordJ]])
print(average)
