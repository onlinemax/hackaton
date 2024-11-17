import time
def timeout(seconds):
    for i in range(seconds):
        time.sleep(1)
        print(i + 1)
def panicked(stats):
    print("You are having a panick attack")
    stats.setEnergy(stats.getEnergy() - 2) 
    stats.setWellbeing(stats.getWellbeing() - 2)
    if (stats.getWellbeing() == 0 or stats.getEnergy() == 0):
        return stats
    stats.info()
    print("You can currently do: ")
    print("-Breathing exercise")
    print("-Grounding exercise")
    print("-Call a friend")
    print("-Do nothing")
    answer = input("Answer:").lower().strip()
    if answer == "breathing exercise":
        print("Breathe in")
        timeout(5)
        print("Hold it")
        timeout(5)
        print("Breathe out")
        timeout(5)
        print("Hold it")
        timeout(5)
        stats.setWellbeing(stats.getWellbeing() + 1)
        stats.setEnergy(stats.getEnergy() + 1)
    elif answer == "grounding exercise":
        print("Name 5 things you can see")
        print("Name 4 things you can touch")
        print("Name 3 things you can hear")
        print("Name 2 things you can smell")
        print("Name 1 things you can taste")
        stats.setWellbeing(stats.getWellbeing() + 1)
        stats.setEnergy(stats.getEnergy() + 2)
    elif answer == "call a friend":
        stats.setWellbeing(stats.getWellbeing() + 2)
        stats.setEnergy(stats.getEnergy() + 1)
    return stats