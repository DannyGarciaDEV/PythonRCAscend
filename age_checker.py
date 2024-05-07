
#Create a conditonal that checks their age
#If under 16, tell them they can not drive
#If under 18, tell them they can't hate from outside the club, because they can't even get in
#If under 21, tell them they can not drink
#If under 25, tell them they can not rent cars affordably
#If under 30, tell them they can not rent fancy cars affordably
#If under over 30, tell them there is nothing left to look forward too



age = int(input("Enter your age: "))

if age < 16:
    print("Sorry, you cannot drive.")
elif age < 18:
    print("You can't hate from outside the club, because you can't even get in.")
elif age < 21:
    print("Sorry, you cannot drink.")
elif age < 25:
    print("Sorry, you cannot rent cars affordably.")
elif age < 30:
    print("Sorry, you cannot rent fancy cars affordably.")
else:
    print("There's nothing left to look forward to.")
    
    