

"""print("Hello World")
print("Hello again")
print("I like typing this")
print("This is fun")
print("Yay! Printing!")
print("I'd much rather you 'not'")
print('I "said" do not touch this')

print("Roosters", 100 -(25*3)%4)

# Variables and Names in Python
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars * space_in_a_car
average_passenger_per_car = passengers / cars_driven

print("There are", cars, "available cars")
print("There are only", drivers, "drivers available")
print("We can transport", carpool_capacity, "people today")
print("We need to put about", average_passenger_per_car, "in each car")


# More variables and printing
my_name     = "Achyut Ray"
my_age      = "22"
my_height   = "6'0"
my_weight   = "180"
my_eyes     = "Brown"
my_teeth    = "White"
my_hair     = "Black"
total       = my_age + my_height + my_weight
print(f"Let's talk about {my_name}")
print(f"He's {my_height} feet tall")
print(f"He weighs {my_weight}")
print(f"Adding strings looks like this: {total}")


types_of_people = 10
x = f"There are {types_of_people} types of people in the world"

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: {y}")

hilarious = False       # To use boolean operators in Python, the first letter is capital: False, and or True!
funny = True
attempt_at_humor = False
joke_evaluation = "Isn't that joke so funny? {}, {}, {}"

print(joke_evaluation.format(hilarious, funny, attempt_at_humor))        
#format is used to enter in variables into the string at a later point. They are entered into the string respective to their position in the container string


#More Printing
print("Mary had a little lamb.")
print("Its fleece was white as {}".format("snow"))
print("And everywhere that Mary went.")
print("."*10) #Prints the "." symbol ten times

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"
print(end1 + end2 + end3 + end4 + end5 + end6, end=" ") #Default end of line character as a result of using print() is a \n (newline character), using end=" " allows to terminate a string with a blank space
## or any other character defined inside the ""
print(end7 + end8 + end9 + end10 +  end11 + end12)


##Printing, Printing
formatter = "{} {} {} {}"
print(formatter.format(1,2,3,4))
print(formatter.format("One", "Two", "Three", "Four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own Text here",
    "Maybe a poem",
    "Or a song about fear"
))
"""

#printing, printing, printing
##days = "Mon Tue Wed Thu Fri Sat Sun"
#months = "Jan\nFeb\nMar\nApril\nMay\nJune\nJuly\August\nSeptember\nOctober\nNovember\nDecember"

#print("Here are the days:", days)
#print("Here are the months: ", months)
#print("""
#With 3 double quotes, I can type as much as I want. There are no restrictions on the number of lines here
#""")

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)