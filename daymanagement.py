from datetime import datetime
import requests
import random

my_day = "My day's Things To Do: "
print(my_day.center(70))

quotes_api = "https://type.fit/api/quotes"
response = requests.get(quotes_api)
# print(response.status_code)
# print(response.json)
quote = response.json()[0]
print(quote)
accomplishes = []
today = datetime.now()
whole_today = today.strftime("%A-%d-%m-%Y %H:%M:%S")
print(whole_today)
while True:
        Do_the_things = input("Things to accomplish: ")
        if Do_the_things == '':
         print(f"{whole_today}: {accomplishes} That's it for today!")
         break
        accomplishes.append(Do_the_things)
        print(accomplishes)

    

