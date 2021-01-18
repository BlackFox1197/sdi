# Datasources
The description of all used datasources.

## S1
* StoneOvenPizza(SOPID, PizzaName, nurishment, total)
* Customer(CID, PIID, FirstName, LastName)
* PaymentInfos(PIID, CreditCardNumber, ccv, expDate)
* Order(OID, CID, orderCode, totalAmount, Adress)
* OrderItem(PID, OID)

## S2
* Pizza(PID, title, nurishment, price)
* User(UID, FirstName, LastName, CCNumber, ccv, expDate)
* Order(OID, UID, orderNumber, Sum, AID)
* InOrder(OID, PID)
* Adress(AID, User, street, city, zip)

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
* CreditCardNumber, ccv, expDate in User is CCInfo in mediated
* first and last name in User is name in mediated
* street, city, zip in Adress is adress in mediated

# Homogenities
* title in Pizza is pizzaName in mediated
* sum in order is totalAmount in mediated
* nurishment in Pizza is nutrition in mediated