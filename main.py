import random 

class Die:
    def __init__(self, sides):
        self.sides = sides 

    def roll(self):
        return random.randint(1, self.sides)
    
    def single_event(self):
        return 1 / self.sides 

    def rolls(self, number):
        dice_rolled = []
        for x in range(number):
            dice_rolled.append(self.roll())
        return dice_rolled

#creating one die 
d1 = Die(6)
#rolling that dice 
print(d1.roll())
#rolling multiple die 
print(d1.rolls(2))
#probability of a single event 
print(d1.single_event())