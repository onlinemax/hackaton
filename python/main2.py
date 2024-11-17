import random
from panicked import panicked
global current_time 
global attack_time
class Stats:
    def getWillpower(self):
        return self.willpower
    def getWellbeing(self):
        return self.wellbeing
    def getEnergy(self):
        return self.energy
    def setWillpower(self, willpower):
        self.willpower = willpower
    def setWellbeing(self, wellbeing):
        self.wellbeing = wellbeing
    def setEnergy(self, energy):
        self.energy = energy 
    def __init__(self, maxStat):
        self.willpower = random.randint(maxStat["willpower"]-5, maxStat["willpower"])
        self.energy = random.randint(maxStat["energy"]-5, maxStat["energy"])
        self.wellbeing = random.randint(maxStat["wellbeing"]-5, maxStat["wellbeing"])
        self.max_stats = maxStat
    def canDo(self, task: dict):
        if "startTime" in task:
            if task["startTime"] > current_time or current_time > task["endTime"]:
                return False
        return task["utilisations"] > 0 and self.willpower >= -1 * task["willpower"] and self.energy >= -1 * task["energy"] and self.wellbeing > -1 * task["wellbeing"] 
    def do(self, task):
        if not self.canDo(task):
            return False
        self.willpower = min(self.willpower + task["willpower"], self.max_stats["willpower"])
        self.energy = min(self.energy + task["energy"], self.max_stats["energy"])
        self.wellbeing = min(self.wellbeing + task["wellbeing"], self.max_stats["wellbeing"])
        task["utilisations"] -= 1 
        return True
    def info(self):
        print(f"Your current stats: wellbeing: {self.wellbeing}, energy: {self.energy}, willpower: {self.willpower}")
    def hasLost(self):
        return self.wellbeing <= 0 or self.energy <= 0 or self.willpower <= 0
    def __str__(self):
        return f"{{willpower: {self.willpower}, energy: {self.energy}, wellbeing: {self.wellbeing}, max_stats {self.max_stats}}}"

class Location:

    def __init__(self, name):
        self.name = name
    def getTasks(self):
        return self.tasks
    def addTasks(self, tasks):
        self.tasks = tasks
        return self
    def addTask(self, name, task):
        self.tasks[name] = task
        
def formated_time(time):
    return f"{int(time)}h{"00" if (time % 1) == 0.0 else "30"}"
def start_game():
    print("Welcome to the life of Lea, a university student!")
    print("Today's schedule:")
    print("9-11am class")
    print("12-2pm lunch with friend")
    print("2-5pm employment")

    print("")
    print("Which impairment do you want to have today?")
    print("Choices: panic attacks/low motivation/both/none")
    answer = input("Answer:").lower().strip()
    max_stats = {"willpower" }
    if answer=="low motivation" or answer=="both":
        max_stats = {"willpower": 7, "energy": 7, "wellbeing": 7}
    else:
        max_stats = {"willpower": 10, "energy": 10, "wellbeing": 10}
    if answer=="panic attacks" or answer=="both":
        # attack_time = random.randint(9*2, 21*2)/2
        global attack_time
        attack_time = 11.5
    return  max_stats
def choose_task(tasks, stat):
    choice = None
    canDoAtask = False
    while choice == None:
        print("You can currently do")
        for task in tasks:
            if not stat.canDo(tasks[task]):
                continue
            canDoAtask = True
            print(f"-{task}")
        print("-end game")
        if not canDoAtask:
            break 
        answer = input("What do you choose: ")
        for task in tasks:
            if answer == "end game":
                return answer
            if answer == task and stats.canDo(tasks[task]):
                choice = task
                break
    return choice
def do_task(choice: str, tasks: dict, stats: Stats):
    stats.do(tasks[choice])
def run_task():
    pass
max_stats = start_game()
print(attack_time)
stats = Stats(max_stats)
wakeup_time = random.randint(int(7*2), int(9*2))/2

print(f"You woke up at {formated_time(wakeup_time)}")
current_time = wakeup_time

locations = [
    Location("home"),
    Location("school")
]
location = locations[0] 
location.addTasks({
    "breakfast": {"utilisations": 1, "willpower": -1, "energy": 3, "wellbeing": 1, "startTime": 7.0, "endTime": 10.0},
    "snooze": {"utilisations": 2, "willpower": 2, "energy": -1, "wellbeing": -1},
    "workout": {"utilisations": 2, "willpower": -2, "energy": 2, "wellbeing": 2},
    "meditate": {"utilisations": 2, "willpower": -1, "energy": 1, "wellbeing": 3},
    "homework": {"utilisations": 4, "willpower": -2, "energy": 1, "wellbeing": 3},
    "scroll": {"utilisations": 1000, "willpower": 1, "energy": 0, "wellbeing": -1},
    "go to school": {"utilisations": 1, "willpower": -1, "energy": -1, "wellbeing": 1, "startTime": 9.0, "endTime": 11.0},
    "see your friend": {"utilisations": 1, "willpower": -1, "energy": 2, "wellbeing": 3, "startTime": 12.0, "endTime": 14.0},
})
locations[1].addTasks({
    "listen in class": {"utilisations": 16, "willpower": 0, "energy": 0, "wellbeing": 1, "startTime": 9.0, "endTime": 10.5},
    "go back home": {"utilisations": 1, "willpower": 0, "energy": 1, "wellbeing": 2, "startTime": 11.0, "endTime": 22.0},
})
while True:
    print("\n")
    print(f"It is currently: {formated_time(current_time)}")
    print(f"You are currently in: {location.name}")
    if location.name != "school" and current_time > 9.0 and current_time < 11.0:
        print("Your suppose to be in school")
        stats.wellbeing -= 1
    stats.info()
    if location.name == "school" and current_time < 11.0:
        choice = "listen in class"
    else:
        choice = choose_task(location.getTasks(), stats)
    if choice == None:
        print("You can't do anything")
        break
    elif choice == "end game":
        print("Bye bye")
        break
    do_task(choice, location.getTasks(), stats);
    if choice == "go to school":
        stats.setWillpower(stats.getWillpower() - 1)
        location = locations[1]
    elif choice == "go back home":
        location = locations[0]
    if stats.hasLost():
        print("You have lost ;(")
        break
    if attack_time == current_time:
        panicked(stats)
    current_time += 0.5
