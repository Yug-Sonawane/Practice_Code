# This Calculate.py Made by Yug-Sonawane

# Simple code for User Data
num1= float(input("Enter Your First Number:"))
num2= float(input("Enter Your Second Number:"))

# Select the opreaton
op= input("Select Opreation by SR.NO \n 1.ADDITION \n 2.SUBTRACTION \n 3.MULTIPLICATION \n 4.DIVISION \n 5.REMAINDER \n 6.FLOOR \n 7.EXPONENTIAL \n 8.SQUARE ROOT \n 9.CUBE ROOT \n 10.AVERAGE \n 11.MATRIX MULTIPLICATION \n ")

# Now main Code of calculator
if op=='1':
    print("Addition of", num1, "and", num2, "is", num1+num2)

elif op=='2':
    print("Substraction of", num1, "and", num2, "is", num1-num2)

elif op=='3':
    print("Multiplication of", num1, "and", num2, "is", num1*num2)

elif op=='4':
    print("Divison of", num1, "by", num2, "is", num1/num2)

elif op=='5':
    print("Remainder of", num1, "divide by", num2, "is", num1%num2)

elif op=='6':
    print("Floor of", num1, "divide by", num2, "is", num1//num2)

elif op=='7':
    print("Exponential value of", num1, "power", num2, "is", num1**num2)

elif op=='8':
    print("Square root of", num1, "is", num1**(1/2))

elif op=='9':
    print("Cube root of", num1, "is", num1**(1/3))

elif op=='10':
    print("Average of", num1, "and", num2, "is", (num1+num2)/2)

elif op=='11':
    print("Matrix multiplication of", num1, "and", num2, "is", num1@num2)

else :
    print("Error")
