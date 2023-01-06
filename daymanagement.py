from datetime import datetime
import requests
import json

my_day = "My day's Things To Do: "
print(my_day.center(70))
def jprint(obj):
    text = json.dumps(obj, sort_keys =True, indent=4)
    print(text)
response = requests.get("https://type.fit/api/quotes")
print(response.json)
accomplishes = []
today = datetime.now()
whole_today = today.strftime("%A-%d-%m-%Y %H:%M:%S")
while True:
        Do_the_things = input("Things to accomplish: ")
        if Do_the_things == '':
         print(f"{whole_today}: {accomplishes} That's it for today!")
         break
        accomplishes.append(Do_the_things)
        print(accomplishes)

    

