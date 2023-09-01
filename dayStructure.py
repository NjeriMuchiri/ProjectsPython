#!/usr/bin/python
"""This program just list my days to do
plus a nice quote"""
from datetime import datetime
import requests
import random


my_day = "My day's Things To Do: "
print(my_day.center(70))


class DaysThings:
			def __init__(self,moment):
						self.moment = moment
						self.addedLists = []
			def now(self):
					now = datetime.now()
					better_format = now.strftime("%A/%d/%B/%Y %H:%M:%S")
					self.moment = better_format
		
			def addTask(self):
					while True:
						Do_the_thing = input("Tasks To Accomplish Today: ")
						if Do_the_thing == '':
							self.addedLists ='\n'.join(self.addedLists)
							print(f"{self.moment}:  \n{self.addedLists}",'\n' "That's it for today!")
							break
					self.addedLists.append(Do_the_thing)
					# print(f"{', '.join(self.addedLists)}" )

			def get_inspired(the_url):
				the_url = "https://type.fit/api/quotes"
				try:
					res = requests.get(the_url)
					if res.status_code == 200:
						data = res.json()
						if data:
							first_quote = data[0]
							the_quoteText = first_quote.get('text')
							author = first_quote.get('author')

							print(f"Quote: {the_quoteText}")
							print(f"Author: {author}")
						else:
							print("No data found in the response")
					else:
						print(f"Request failed with status code: {res.status_code}")
				except requests.exceptions.RequestException as err:
					print(f"Request failed with error: {err}")

didTheThing = DaysThings(moment = "now")
didTheThing.now()
print(didTheThing.moment)
didTheThing.addTask()
didTheThing.get_inspired()
