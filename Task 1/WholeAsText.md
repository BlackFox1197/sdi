# Datasources
The description of all used datasources.

## S1
* Pizza(PID, title, nurishment, price)
* Topping(TID, title, nurishment)
* ToppingOnPizza(TIP, PID)

## S2
* User(UID, Name, CC)

## S3
* Order(OID, User, Sum, AID)
* InOrder(OID, pizza)
* Adress(AID, User, street, city, zip)

# CQ
* getOrdersFromUser(UID, OID, Sum):- User(UID), Order(OID, UID, Sum)
* getAdressFromUser(UID, street, city, zip);- User(UID), Adress(UID, street, city, zip)
* getAdressFromUserOrder(UID, OID, street, city, zip):- User(UID), Order(OID, UID, AID), Adress(AID, UID, street, city, zip)
* getPizzaFromOrder(OID, title):- InOrder(OID, PID), Pizza(PID, title)
* getToppingsFromPizza(PID, pizzaTitle, toppingTitle):- Pizza(PID, pizzaTitle), ToppingOnPizza(TID, PID), Topping(TID, toppingTitle)

# Mediated Schema
* UserOrder(UID, OID, Sum)
* UserAdress(UID, street, city, zip)
* OrderAdress(UID, OID, street, city, zip)
* OrderPizza(pizzaName, OID)
* PizzaTopping(PID, pizzaName, toppingName)

# Heterogenities
* title in Pizza is Pizzaname in mediated