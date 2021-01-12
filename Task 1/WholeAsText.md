## Mediated Scema
* Order(Pizzaname, OID)

## S1
* Pizza(PID, title, nurishment, price)
* Topping(TID, title, nurishment)
* ToppingOnPizza(TIP, PID)

## S2
* User(UID, Name, CC)

## S3
* Order(OID, User, Sum, AID)
* InOrder(OID, pizza)
* Adress(AID, street, city, zip)



# CQ
* getPizzaFromOrder(OID, title):- Order(OID, PID), pizza(PID, title)

# Heterogenities
* title in Pizza is Pizzaname in mediated