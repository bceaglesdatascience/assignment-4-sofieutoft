#ask the user for input on the number of purchases at a store and sales tax
number_of_purchases = int(input("Number of purchases: "))
sales_tax = float(input("Sales tax: "))

#create lists
customers = []
costs = []

#add to lists
i = 1
while i <= number_of_purchases:
    customer = input("Customer: ")
    customers.append(customer)
    cost = float(input("Cost: "))
    costs.append(cost)
    i += 1

#function to add tax
def add_tax(prices, tax):
    for i in range(len(prices)):
        prices[i] += (prices[i] * tax)
    return prices

#run function
total_costs = add_tax(costs, sales_tax)

#create dictionary
purchases = {}
for i in range(len(customers)):
    if customers[i] in purchases:
        purchases[customers[i]] += total_costs[i]
    else:
        purchases[customers[i]] = total_costs[i]

#print dictionary
print(purchases)
