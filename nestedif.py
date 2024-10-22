# task1

place = input("Choose your place. (forrest/cave): ")


if place == "forrest":
    action = input("What do you want to do? (climb tree/cross river) ")

    if action == "climb tree":
        print("You found a birds nest!")
    elif action == "cross river":
        print("You found a boat!")
elif place == "cave":
    action = input("What do you want to do? (light torch/proceed in dark)")
   
    if action == ("light torch"):
        print("You can now see!")
    elif action == ("proceed in dark"):
        print("Watch out for spiders!")
else:
    pass


#task2

attendees = input("Enter number of attendees: ")

venue = "large hall with audio system" if int(attendees) > 100 else "conference room with projector" 
print(venue)
type_of_meal = input("do you want vegetarian? (yes/no):")
# if type_of_meal == "yes":
#     print("Veggie Delight Caterers")
# else:
#     print("Gourmet Meals Caterers")

output = "Veggie Delight Caterers" if type_of_meal == "yes" else "Gourmet Meals Caterers"
print(output)