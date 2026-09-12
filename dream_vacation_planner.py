#Welcome & User Info
#Welcome
print("=====🌍 DREAM VACATION PLANNER 🌍=====")


#User Info
name = input("Enter your name: ")
age = int(input("Enter your age: "))

#chech age 
if age < 18:
    status = "You need a guardian's permission to travel"
else:
    status = "You're eligible to travel solo!"


#Choose a Destination
print("Choose your destination:")
print("1. Paris ($1200)")
print("2. Tokyo ($1500)")
print("3. New York ($1000)")


#Choose variables
choose = int(input("Enter the number of your destiantion:  "))
if choose == 1:
    destination = "Paris"
    price = 1200
    
elif choose == 2:
    destination = "Tokyo"
    price = 1500
    
elif choose == 3:
    destination = "New York"
    price = 1000
    
else:
    destination = "unknown"
    price = 0


# Travel Style
travel_style = input("Do you want economy or luxury? ")
if travel_style.lower() == "economy":
    price = price
elif travel_style.lower() == "luxury":
    price = price + 500
else:
    print("Invalid choice. Defaulting to economy.")


#Number of Travelers
number_of_travelers = int(input("How many people are traveling? "))
total = price * number_of_travelers


#Discount Check
if int(number_of_travelers) >= 4:
    total = total * 0.90
    print("🎉 Group discount applied! 10% off!")
else:
    print("No group discount.")


#Budget Check
budget = float(input("What is your total budget? ($)"))
difference = total - budget
if budget < total:
    print(f"❌ You need ${difference:.2f} more.")
elif budget >= total:
    print("✅ You can afford this trip!")





#User interface 
print("========================")
print()
print("VACATION PLANNER RECEIPT")
print("========================")
print()
print("Traveler        :    " + name)
print("age             :    " + str(age))
print("destination     :    " + destination)
print("travel style    :    " + travel_style)
print("Travelers       :    " + str(number_of_travelers))
print("Price per person:    " + str(price))
print("------------------------------------------------")
print("TOTAL           :    " + str(total) )
print("Budget          :    " + str(budget))
print("Status          :    " + status)
print("========================================")
print("Have a great trip, " + name + "! ✈️")