# 8 kuy level challenge from codewars.com

# Are you playing banjo?
# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!

# The function takes a name as its only argument, and returns one of the following strings:

# name + " plays banjo" 
# name + " does not play banjo"

# Names given are always valid strings.


def are_you_playing_banjo(name):
    if name.lower().startswith('r'):
        #print(f"{name} plays banjo") 
        return f"{name} plays banjo"
    else: 
        #print(f"{name} does not play banjo")
        return f"{name} does not play banjo"

are_you_playing_banjo("Steve")
are_you_playing_banjo("Rick")