from datetime import datetime
import requests

my_day = "My day's Things To Do: "
print(my_day.center(70))
response = requests.get("https://type.fit/api/quotes")
print(response.status_code)
accomplishes = []
today = datetime.now()
whole_today = today.strftime("%A-%d-%m-%Y %H:%M:%S")
while True:
        Do_the_things = input("Things to accomplish: ")
        if Do_the_things == '':
         print(f"{whole_today}: That's it for today!")
         break
        accomplishes.append(Do_the_things)
        print(accomplishes)

    

