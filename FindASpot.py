                   
import random
num = random.randint(1,5)
Places = ["Germany It Is", "France Sounds Fantastic", "Spain Would Be Splendid", "United States, OK", "Switzerland, Sweet", "UK Sounds Like Fun"]
ans = input("Where would you like to go?:" + "\n")
price = input("How much do you want to spend?:" + "\n")

if ans == "Home":
    print(Places[0])
elif ans == "You Pick":
    print(Places[num])


