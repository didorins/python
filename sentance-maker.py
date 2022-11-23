# In this simple program, I defined a function, which checks with conditional if sentance begins with key words that 
# identify it as a question. If true, we return the string with a quesiton mark in the end and format it to capitalize first leter
# To make the program more practical, added complexity with while loop to check if user input ends with specific string
# If it does, we exit the program, if not we append the processed user input with defined function and then return the while loop, asking for more user input.

def sentancemaker(phrase):
    capitalize = phrase.capitalize()
    question = ("How", "What", "Where")
    thanks = ("Thanks", "Thank")

    if  capitalize.startswith(question):
        return "{}?".format(capitalize)
    elif capitalize.startswith(thanks):
        return "{}!".format(capitalize)
    else:
        return "{}.".format(capitalize)

results = []

while True:
    usr_input = input("Enter text to format (type /end to finish): ")
    if usr_input.endswith("/end"):
        break
    else:
        results.append(sentancemaker(usr_input))

print(" ".join(results))