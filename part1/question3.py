################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
class MagicalOven:
    #constructor for the MagicalOven class. 
    def __init__(self):
        self.ingredients = []
        self.output = None
    #allows adding an ingredient to the oven. The ingredient is passed as an argument and is added to the oven's list of ingredients.
    def add(self, item):
        self.ingredients.append(item)

    #sets the oven's output to "snow" and removes all ingredients in the oven, simulating that the oven has frozen the ingredients.
    def freeze(self):
        self.output = "snow"
        self.ingredients = []

    #checks if the oven contains "lead" and "mercury" in its ingredients. If so, it sets the oven's output to "gold."
    def boil(self):
        if "lead" in self.ingredients and "mercury" in self.ingredients:
            self.output = "gold"
        else:
            self.output = None

    #checks if the ingredients in the oven are ["cheese", "dough", "tomato"]. If they are, it sets the oven's output to "pizza." 
    # Otherwise, the output is set to None pizza :().
    def wait(self):
        if all(ingredient in self.ingredients for ingredient in ["cheese", "dough", "tomato"]):
            self.output = "pizza"
        else:
            self.output = "none pizza :c"

    def get_output(self):
        return self.output

#creates and returns an instance of the MagicalOven class
def make_oven():
    return MagicalOven()

# takes a oven object, a list of ingredients, and a temperature as arguments. 
# It then adds the ingredients to the oven and, depending on the temperature, 
# calls the freeze(), boil(), or wait() methods of the oven to perform different transformations. 
def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif 101 <= temperature < 151:
        oven.wait()
    elif temperature >= 100:
        oven.boil()
    
    return oven.get_output()


