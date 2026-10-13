#a) Print Hello World  
print("Hello world")

#b) Create two variables and print their addition  
a=10;
b=20;
print("sum=",(a+b));
  
#c) Print their difference 
a=15;
b=20;
difference=a-b;
print(difference);

#d) Print their multiplication
a=20;
b=13;
mult=(a*b);
print(mult);

#e) Print their division 
a=55;
b=15;
div=(a/b);
print(div);

#f) Print their modulus  
a=35;
b=5;
mod=(a%b);
print(mod);


#2nd method to do all tasks together taking values from user
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
print("Addition:", a+b)
print("Difference:", a-b)
print("Multiplication:", a*b)
print("Division:", a/b)
print("Modulus:", a%b)
