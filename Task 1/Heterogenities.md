# Heterogenities of the Datasources
## Pizza
- Joy has only one pizza class with an size attribute whereas Domina has 3 different pizza classes for all the sizes
	- Domina has 1 base option for size small and 2 base options for the other two (medium and large) at Joy they are the same amount (2)
- Domina has only fixed toppings which are boolean in the pizza table and Joy has an table for toppings and an midtable for selecting

## Customers
- At Domina it is only possible to save one cc cause its saved in the customer data, whereas at Joy there is a 1 to n table for creditcards, so each customer can have multiple cc
- at Domina the adresses are saved as string in the user table, at Joy there is an 1 to n table and an special adress table 

## Orders
- At Domina you can order only with an existing account, so each order is linked to an account. At Joy you can order as guest, the order is linked to an adress and the payment information



