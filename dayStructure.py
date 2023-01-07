from datetime import datetime 
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
              print(f"{self.moment}:  \n{', '.join(self.addedLists)}",'\n',"That's it for today!")
              break
          self.addedLists.append(Do_the_thing)
          print(f"{', '.join(self.addedLists)}" )
          

didTheThing = DaysThings(moment = "now")
didTheThing.now()
print(didTheThing.moment)
didTheThing.addTask()


