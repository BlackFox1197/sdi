# Datasources
The description of all used datasources.

## S1
* StoneOvenPizza(SOPID, PizzaName, nurishment, total)
* Customer(CID, PIID, FirstName, LastName)
* PaymentInfos(PIID, CreditCardNumber, ccv, expDate)
* Order(OID, CID, orderCode, totalAmount, Adress)
* OrderItem(SOPID, OID)

## S2
* Pizza(PID, title, nurishment, price)
* User(UID, FirstName, LastName, CCNumber, ccv, expDate)
* Order(OID, UID, orderNumber, Sum, AID)
* InOrder(OID, PID)
* Adress(AID, UID, street, city, zip)

# CQ
* getTotalAmountFromUser(name, totalAmount):- User(UID, name), Order(UID, totalAmount)
* userOrder(OID, name):- order(OID, UID), user(name, UID)
* getUserCc(CCInfo, name):- user(name, CCInfo)
* getAdressFromUser(name, Adress):- user(name, UID), order(UID, Adress)
* getPizzaFromOrder(orderNumber, pizzaName):- order(OID, orderNumber), orderItem(OID, PID), pizza(PID, pizzaName)

# Mediated Schema
* User(UID, name, CCInfo)
* OrderItem(PID, OID)
* Order(OID, UID, orderNumber, totalCost, Adress)
* Pizza(PID, pizzaName, nutrition, price) 

# Heterogenities
## S1 to mediated Schema:
* CreditCardNumber, ccv, expDate in PaymentInfos is CCInfo in mediated
* first and last name in Customer is name in mediated
## S2 to mediated Schema:
* first and last name in User is name in mediated
* street, city, zip in Adress is adress in mediated


# named Heterogenities
## S1 to mediated Schema:
* StoneOvenPizza Class is Pizza Class in mediated 
* Customer Class is User Class in medited
* nurishment in Pizza is nutrition in mediated
* total in Pizza is price in mediated
* totalAmount in order is totalCost in mediated
* orderCode in order is orderNumber in mediated
## S2 to mediated Schema:
* InOrder Class is OrderItem Class in mediated 
* nurishment in Pizza is nutrition in mediated
* sum in order is totalCost in mediated
* titel in Pizza is pizzaName in mediated