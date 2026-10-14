# Task 01: Shopping Bill
# GST First, Discount After

# 1. Calculate Electronics Bill (18% GST)
def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst


# 2. Calculate Fashion Bill (13% GST)
def calculateFashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
    return total + gst


# 3. Calculate Food Bill (7% GST)
def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


# 4. Calculate Total Bill
def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


# 5. Calculate Discounted Bill (20% Discount)
def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount


# Main Calculation (No input required)
a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

# Display Output
print("Electronics Bill:", electronics)
print("Fashion Bill:", fashion)
print("Food Bill:", food)
print("Total after GST:", total)
print("20% Discount:", discount)
print("Final Payable Amount:", final_amount)