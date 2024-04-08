"""
PowerOfTen
"""
# Provide your solution here
number = int(input("Give me an integer of 3 digits at max:" ))

if number < 0:
    print("Number cannot be negative")
elif number >= 1000:
    print("Number has more than 3 digits")

"""
Cash Box
"""
# Provide your solution here
budget = int(input("What's your current budget?\n"))
print("Hello! Your budget is" + str(budget) + ". But you still have to pay!How much are you willing to pay?")

amount_received = int(input("How much?"))

if amount_received < 0:
    print("Incorrect. What's your current budget?")

elif amount_received <= 50:
    print("Negative received amount is invalid.")

else amount_received >= 51:
    print("Your change is 25 Euros")


