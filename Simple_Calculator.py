# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("Welcome to the calculator.")

while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
       num1 = float(input("Enter a number: "))
       num2 = float(input("Enter another number: "))
       result = str(num1 + num2)
       print("The answer is " + result)
   elif user_input == "subtract":
       num1 = float(input("Enter a number: "))
       num2 = float(input("Enter another number: "))
       result = str(num1 - num2)
       print("The answer is " + result)
   elif user_input == "multiply":
       num1 = float(input("Enter a number: "))
       num2 = float(input("Enter another number: "))
       result = str(num1 * num2)
       print("The answer is " + result)
   elif user_input == "divide":
       num1 = float(input("Enter a number: "))
       num2 = float(input("Enter another number: "))
       result = str(num1 / num2)
       print("The answer is " + result)
   else:
      print("Unknown input")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
