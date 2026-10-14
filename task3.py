# 1. Calculate Food Bill with 5% GST
def calculateFoodGST(a, b):
    total = a + b
    return total + (total * 5 / 100)


# 2. Calculate Drinks Bill with 12% GST
def calculateDrinksGST(c, d):
    total = c + d
    return total + (total * 12 / 100)


# 3. Calculate Dessert Bill with 7% GST
def calculateDessertGST(e):
    return e + (e * 7 / 100)


# 4. Calculate Total Cafe Bill
def totalBill(a, b, c, d, e):
    return (calculateFoodGST(a, b)
            + calculateDrinksGST(c, d)
            + calculateDessertGST(e))


# 5. Calculate Final Bill After 20% Discount
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


# Sample amounts
a = 100
b = 100
c = 100
d = 100
e = 100

# Calculate bills
food = calculateFoodGST(a, b)
drinks = calculateDrinksGST(c, d)
dessert = calculateDessertGST(e)

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

# Display output
print("Food Bill:", round(food, 2))
print("Drinks Bill:", round(drinks, 2))
print("Dessert Bill:", round(dessert, 2))
print("Total after GST:", round(total, 2))
print("20% Discount:", round(discount, 2))
print("Final Payable Amount:", round(final_amount, 2))